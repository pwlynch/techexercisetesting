import os

def before_feature(context, feature):
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    context.client = app.test_client()
    init_db()

def after_feature(context, feature)
    os.close(context.db)
    os.unlink(app.config['DATABASE'])
