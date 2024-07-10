from roboflow import Roboflow
rf = Roboflow(api_key="TGVK9JFYaCxCeaLmZF80")
project = rf.workspace("valkyrie").project("data")
version = project.version(1)
dataset = version.download("yolov9")