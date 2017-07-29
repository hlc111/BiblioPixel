import copy, gitty, functools, sys
from . import aliases, importer
from .. animation import runner
from .. project import data_maker
from .. layout.geometry import gen_matrix
from .. layout.multimap import MultiMapBuilder
from .. util import files
from .. util import log

RESERVED_PROPERTIES = 'name', 'data'


def _make_drivers_and_coord_map(driver, drivers, make_object):
    if not drivers:
        return [make_object(**driver)], None

    if driver:
        # driver is a default for each driver.
        drivers = [dict(driver, **d) for d in drivers]

    build = MultiMapBuilder()

    def make_driver(width, height, matrix=None, **kwds):
        build.addRow(gen_matrix(width, height, **(matrix or {})))
        return make_object(width=width, height=height, **kwds)

    return [make_driver(**d) for d in drivers], build.map


def make_animation(layout, animation, run=None):
    reserved = {p: animation.pop(p, None) for p in RESERVED_PROPERTIES}
    animation = importer.make_object(layout, **animation)

    # Add the reserved properties back in.
    for k, v in reserved.items():
        (v is not None) and setattr(animation, k, v)

    animation.set_runner(runner.Runner(**(run or {})))
    return animation


def project_to_animation(desc, default):
    project = aliases.resolve(default or {}, desc)

    animation = project.pop('animation', None)
    driver = project.pop('driver', None)
    drivers = project.pop('drivers', None)
    layout = project.pop('layout', None)
    maker = project.pop('maker', None)
    path = project.pop('path', None)
    run = project.pop('run', None)

    if project:
        log.error('Did not understand sections %s', project)

    if not animation:
        raise ValueError('animation was not specified in project')

    if not layout:
        raise ValueError('layout was not specified in project')

    if not (driver or drivers):
        raise ValueError('Projects has neither driver nor drivers sections')

    gitty.sys_path.extend(path or '')
    maker = data_maker.Maker(**(maker or {}))
    make_object = functools.partial(importer.make_object, maker=maker)

    drivers, coord_map = _make_drivers_and_coord_map(
        driver, drivers, make_object)
    coord_map = layout.pop('coordMap', None) or coord_map
    layout_object = make_object(drivers, coordMap=coord_map, **layout)
    return make_animation(layout_object, animation, run)
