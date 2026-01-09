from LSBC_Backend.config.mongodb import db
from bson import ObjectId
from datetime import datetime

def create_club(club_data):
    club_data['created_at'] = datetime.utcnow()
    result = db.clubs.insert_one(club_data)
    return str(result.inserted_id)

def delete_club(club_id):
    # Delete all players and coaches associated with the club first
    db.players.delete_many({"club_id": ObjectId(club_id)})
    db.coaches.delete_many({"club_id": ObjectId(club_id)})
    result = db.clubs.delete_one({"_id": ObjectId(club_id)})
    return result.deleted_count > 0

def create_player(club_id, data):
    count = db.players.count_documents({"club_id": ObjectId(club_id)})
    
    if count >= 20:
        raise ValueError("Maximum of 20 players allowed")

    # Convert date to datetime for MongoDB compatibility
    if 'dob' in data and data['dob']:
        data['dob'] = datetime.combine(data['dob'], datetime.min.time())
    
    data["club_id"] = ObjectId(club_id)
    result = db.players.insert_one(data)
    return str(result.inserted_id)

def update_player(player_id, data):
    if 'dob' in data and data['dob']:
        data['dob'] = datetime.combine(data['dob'], datetime.min.time())
    result = db.players.update_one({"_id": ObjectId(player_id)}, {"$set": data})
    return result.modified_count > 0

def delete_player(player_id):
    result = db.players.delete_one({"_id": ObjectId(player_id)})
    return result.deleted_count > 0

def create_coach(club_id, data):
    data['club_id'] = ObjectId(club_id)
    result = db.coaches.insert_one(data)
    return str(result.inserted_id)

def update_coach(coach_id, data):
    result = db.coaches.update_one({"_id": ObjectId(coach_id)}, {"$set": data})
    return result.modified_count > 0

def delete_coach(coach_id):
    result = db.coaches.delete_one({"_id": ObjectId(coach_id)})
    return result.deleted_count > 0

def get_clubs():
    clubs = list(db.clubs.find())
    for club in clubs:
        club_id = club["_id"]
        
        # Get players and convert their ObjectIds to strings
        players = list(db.players.find({"club_id": club_id}))
        for player in players:
            player["_id"] = str(player["_id"])
            player["club_id"] = str(player["club_id"])
        
        # Get coaches and convert their ObjectIds to strings
        coaches = list(db.coaches.find({"club_id": club_id}))
        for coach in coaches:
            coach["_id"] = str(coach["_id"])
            coach["club_id"] = str(coach["club_id"])
        
        club["players"] = players
        club["coaches"] = coaches
        club["_id"] = str(club["_id"])
    return clubs