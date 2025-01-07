import sys
sys.path.append(r"C:\Program Files\DIgSILENT\PowerFactory 2024 SP4\Python\3.11")
import powerfactory as pf
app = pf.GetApplication()
from pandapower.converter.powerfactory import from_pfd
from pandapower.converter.powerfactory.validate import validate_pf_conversion
net = from_pfd(app, prj_name="50 Hz")
val = validate_pf_conversion(net)