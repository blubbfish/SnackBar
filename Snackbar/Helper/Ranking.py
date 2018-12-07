from Snackbar import db
from sqlalchemy.sql import func, and_, extract
from Snackbar.Models.User import User
from Snackbar.Models.History import History
from datetime import datetime

def get_rank(userid, itemid):
  tmp_query = db.session.query(User.userid, func.count(History.price)).outerjoin(History, and_(User.userid == History.userid, History.itemid == itemid, extract('month', History.date) == datetime.now().month, extract('year', History.date) == datetime.now().year)).group_by(User.userid).order_by(func.count(History.price).desc()).all()
  user_id = [x[0] for x in tmp_query]
  item_sum = [x[1] for x in tmp_query]
  idx = user_id.index(userid)
  rank = idx + 1
  if rank == len(user_id):
    upperbound = item_sum[idx - 1] - item_sum[idx] + 1
    lowerbound = None
  elif rank == 1:
    upperbound = None
    lowerbound = item_sum[idx] - item_sum[idx + 1] + 1
  else:
    upperbound = item_sum[idx - 1] - item_sum[idx] + 1
    lowerbound = item_sum[idx] - item_sum[idx + 1] + 1
  return {'rank': rank, 'upperbound': upperbound, 'lowerbound': lowerbound}
