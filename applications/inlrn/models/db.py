################################################################
####db.py#######################################################
################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

################################
####database_conntection########
################################  

if not request.env.web2py_runtime_gae:
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

################################
####auth_settings###############
################################ 
## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'
## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

################################################################
####database_tables#############################################
################################################################

################################
####academy#####################
################################  
db.define_table('academy',
    Field('url_title','string'),
    Field('title','string'),
    Field('description','string'),

)


################################
####assignment##################
################################  
db.define_table('assignment',
    Field('course_id','string', readable=False, writable=False),
    Field('title','string'),
    Field('description','text'),
)

################################
####assignment_question#########
################################  
db.define_table('assignment_question',
    Field('assignment_id','string'),
    Field('title','string'),
    Field('question_type','string'),
    Field('question_choices','list:string'),
    Field('question_answer','list:string'),
    Field('description','text'),
)

################################
####course_member###############
################################  
import datetime
db.define_table('course_member',
    Field('auth_user_id','string'),
    Field('course_id','string'),
    Field('member_type','string'),
    Field('join_time','datetime', default=datetime.datetime.utcnow()),
)

################################
####academy_tag#################
################################ 
db.define_table('academy_tag',
    Field('academy_id','string'),
    Field('tag','string'),
)

################################
####course######################
################################ 
db.define_table('course',
    Field('academy_id_array','list:integer'),
    Field('auth_user_id','string'),
    Field('url_title','string'),
    Field('title','string'),
    Field('description','text')
)

################################
####course_tag##################
################################ 
db.define_table('course_tag',
    Field('course_id','string'),
    Field('tag','string'),
)

################################
####course_page#################
################################ 
db.define_table('course_page',
    Field('course_id','string', readable=False, writable=False),
    Field('title','string'),
    Field('page_content','text'),
)

################################
####thread######################
################################ 
db.define_table('thread',
    Field('academy_course_id_array','list:integer'),
    Field('title','string'),
    Field('thread_content','text'),

)

################################
####thread_tag##################
################################ 
db.define_table('thread_tag',
    Field('academy_id','integer'),
    Field('tag','string'),
)
