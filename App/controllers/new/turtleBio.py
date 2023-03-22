from App.models import TurtleBio
from App.database import db

import json

#Create turtle_bio object
def create_turtle_bio(
                    turtle_id,
                    length,
                    width,
                    weight
                    ):
    
    newturtle_bio = TurtleBio(
                    turtle_id,
                    length,
                    width,
                    weight
                    )
    
    db.session.add(newturtle_bio)
    db.session.commit()
    return newturtle_bio

#Get turtle_bio by turtle_bio_id
def get_turtle_bio(turtle_bio_id):
    return TurtleBio.query.get(turtle_bio_id)

#Get all turtle_bios
def get_all_turtle_bio_json():
    turtle_bios = TurtleBio.query.all()
    if not turtle_bios:
        return []
    return [turtle_bio.toJSON() for turtle_bio in turtle_bios]
    
#Delete an turtle_bio by excavation_id
def delete_turtle_bio(turtle_bio_id):
    turtle_bio = get_turtle_bio(turtle_bio_id)
    if turtle_bio:
        db.session.delete(turtle_bio)
        return db.session.commit()
    return None