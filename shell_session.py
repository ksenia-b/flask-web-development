#wrong way, would not work
from hello import app
from flask import current_app
#
# current_app.name

# will work, right one:
app_ctx = app.app_context()
app_ctx.push()
print(current_app.name)
app_ctx.pop()