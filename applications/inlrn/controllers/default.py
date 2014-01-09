################################################################
####controllers#################################################
################################################################
  
################################
####about#######################
################################
def about():
   
    return dict()

################################
####academy#####################
################################                    
def academy():
    
    #if 
    try:
        academy_from_url = db(db.academy.url_title == request.args(0)).select()
        academy_id_from_url = db(db.academy.url_title == request.args(0)).select()[0]['id']

        academy_courses = db(db.course.academy_id_array.contains(academy_id_from_url)).select()


    except IndexError:
        redirect(URL('academies'))
   
    return dict(
        
        academy_id_from_url=academy_id_from_url,
        academy_from_url=academy_from_url,
        academy_courses=academy_courses,
    )

################################
####academies###################
################################        
def academies():

    academy_list = db(db.academy).select()
   
    return dict(academy_list=academy_list)

################################
####account#####################
################################        
def account():
   
    return dict()  
    
################################
####contact#####################
################################
def contact():
   
    return dict()

################################
####course######################
################################            
def course():
   
    try:
        course_from_url = db(db.course.url_title == request.args(0)).select()[0]['title']
    except IndexError:
        redirect(URL('courses'))
    
    
    return dict(course_from_url=course_from_url)
   

################################
####courses#####################
################################        
def courses():

    course_list = db(db.course).select()
   
    return dict(course_list=course_list)            

################################
####discover####################
################################        
def discover():

    return dict()

################################
####faq#########################
################################                  
def faq():

    return dict()

################################
####feed########################
################################
def feed():
   
    return dict()
    
################################
####inbox#######################
################################ 
def inbox():
   
    return dict()

################################
####index#######################
################################        
def index():
   
    return dict()

################################
####mission#####################
################################        
def mission():

    return dict()

################################
####member######################
################################        
def member():

    try:
        username_from_url = db(db.auth_user.username == request.args(0)).select()[0]['username']
    except IndexError:
        redirect(URL('members'))
    
    
    return dict(username_from_url=username_from_url)
    
################################
####members#####################
################################        
def members():
   
    return dict()     

################################
####notifications###############
################################        
def notifications():
   
    return dict() 
################################
####privacy#####################
################################
def privacy():
   
    return dict()

def stats():
   
    return dict()   

################################
####search######################
################################        
def search():
   
    return dict()  
     
################################
####tag#########################
################################          
def tag():
   
    return dict()
    
################################
####tags########################
################################          
def tags():
   
    return dict()   

################################
####terms#######################
################################
def terms():
   
    return dict()

################################
####thread######################
################################          
def thread():
   
    return dict()

################################
####threads#####################
################################          
def threads():
   
    return dict()
    
################################
####transparency################
################################
def transparency():

    return dict()
    

################################################################
####ajax########################################################
################################################################    
            
################################################################
####helpers#####################################################
################################################################

################################
####download####################
################################   
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

################################
####call########################
################################ 
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

################################
####data########################
################################ 
@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
