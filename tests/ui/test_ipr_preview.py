"""
Copyright 2023, Pytrophysics developers.

Licensed under GNU GPL 3.0 or later.
See COPYING.txt for more information (you should have received a copy of the GNU General Public License 3
along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.txt>).
"""

import os

from tests.tests_helper import (set_current_path, init_config)

current_path = os.path \
    .abspath(__file__) \
    .split("\\")

current_path = set_current_path(current_path)


def test_ipr_preview(qtbot):
    window = init_config(qtbot, current_path)

    tab = window.tabs[2] \
                .tabs[10] \
                .tabs[5]

    assert tab.ipr_curve_to_draw_cbo \
        .itemText(0) == "F1"


    assert tab.ipr_curve_to_delete_cbo \
        .itemText(0) == "F1"
