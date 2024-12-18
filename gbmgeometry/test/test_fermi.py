from gbmgeometry.spacecraft.fermi import Fermi
from gbmgeometry import PositionInterpolator
from gbmgeometry.utils.package_utils import get_path_of_data_file


def test_fermi_constructor(interpolator):

    fermi = Fermi(interpolator.quaternion(0), interpolator.sc_pos(0))


def test_fermi_plotting(interpolator):

    fermi = Fermi(interpolator.quaternion(0), interpolator.sc_pos(0))

    fermi.plot_fermi()
