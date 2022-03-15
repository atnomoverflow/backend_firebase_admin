
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate(r"C:\Users\monta\Desktop\Test Ground\FlutterFirebaseAR\script for firebase\arreconstruction-cb284-firebase-adminsdk-xsh3p-0d22ffeff1.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://arreconstruction-cb284-default-rtdb.europe-west1.firebasedatabase.app/'})
def requestHandler(event):
    if event.data:
        if type(event.data) is dict and event.data.get("state") is not None and event.data.get("state")==0:
            db.reference("/requestReconstruction").child(event.path[1:]).update({
                "model_uri":"https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/SheenChair/glTF/SheenChair.gltf",
                "state":2
            })
                
db.reference("/requestReconstruction").listen(requestHandler)