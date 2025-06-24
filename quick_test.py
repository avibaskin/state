

import sys, types
sys.modules['zclip'] = types.ModuleType('zclip')   # stub: makes import zclip work

import sys, importlib, state.sets.models as _m
sys.modules["models"] = _m                     # top-level alias

from inference_module import Predictor         # import succeeds now
m = Predictor.load_pretrained(device="cpu")
print("✅  Model loaded")
print(m.predict("dexamethasone").head())
