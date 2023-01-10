from ci_sandbox.magicgui_related.container import get_default_widget
from magicgui.widgets import SpinBox

def test_default_widget():
    widget_class, opts = get_default_widget("x", 1.0, int)
    assert widget_class is SpinBox

    c = widget_class(**opts)
    assert isinstance(c, SpinBox)
