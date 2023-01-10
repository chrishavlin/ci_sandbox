from ci_sandbox.magicgui_related.container import get_default_widget
from magicgui.widgets import SpinBox
from magicgui import use_app
import pytest

# following magicgui testing approach, create a backend fixgure
@pytest.fixture(scope="module", params=["ipynb", "qt"])
def backend(request):
    return request.param

def test_default_widget(backend):
    app = use_app(backend)

    widget_class, opts = get_default_widget("x", 1.0, int)
    assert widget_class is SpinBox

    c = widget_class(**opts)
    assert isinstance(c, SpinBox)

    c.close()
