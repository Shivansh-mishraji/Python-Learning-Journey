# services.py — business logic
# import Session from sqlalchemy.orm
# import models and schemas (from models import User, Application etc.)
# put the @timer decorator here too
#
# write these 6 service functions:
# create_user(db, data) -> User
# get_user(db, user_id) -> User          ← raise 404 if not found
# add_application(db, data) -> Application  ← raise 404 if user not found
#                                            ← raise 400 if status is invalid
# get_user_applications(db, user_id) -> list[Application]
# update_status(db, app_id, new_status) -> Application  ← raise 400 if invalid status
#                                                        ← raise 404 if app not found
# delete_application(db, app_id) -> None   ← raise 404 if not found
#
# valid statuses: "applied", "interview", "offer", "rejected"
