#-*- coding:utf-8 -*-

import config
from app.database import db
from sqlalchemy import event

class BugFix(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1023))
    text = db.Column(db.Text)
    date = db.Column(db.Date)
    status = db.Column(db.String(1))
    timefj = db.Column(db.Time)
    createdate = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return self.id

    def to_dict(self):
        return {'name':       self.name,
                'text':       self.text,
                'date':       str(self.date),
                'status':     self.status,
                'createdate': str(self.createdate)}

@event.listens_for(BugFix, 'after_insert')
@event.listens_for(BugFix, 'after_update')
def send_bugs(mapper, connection, target):
    if hasattr(config, 'BUGFIX_URL') and hasattr(config, 'BUGFIX_PROJECT'):
        import urllib2, json
        data = {'json': [bug.to_dict() for bug in BugFix.query.all()], 'project': config.BUGFIX_PROJECT}
        jsn = json.dumps(data)
        req = urllib2.Request(config.BUGFIX_URL, jsn, headers={'Content-Type': 'application/json'})
        try:
            urllib2.urlopen(req)
        except:
            pass
