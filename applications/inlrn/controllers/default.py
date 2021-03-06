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
    
    try:
        academy_from_url = db(db.academy.url_title == request.args(0)).select()
        academy_id_from_url = db(db.academy.url_title == request.args(0)).select()[0]['id']

        academy_courses = db(db.course.academy_id_array.contains(academy_id_from_url)).select()

        academy_member_list = db(db.academy_member.academy_id == academy_id_from_url).select()

    except IndexError:
        redirect(URL('academies'))
   
    return dict(
        
        academy_id_from_url=academy_id_from_url,
        academy_from_url=academy_from_url,
        academy_courses=academy_courses,
        academy_member_list=academy_member_list,
    )

################################
####academies###################
################################        
def academies():

    academy_list = db(db.academy).select()
    academy_tag_list = db(db.academy_tag).select()
   
    return dict(
        academy_list=academy_list,
        academy_tag_list=academy_tag_list,
    )

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

    form_create_question = ''
    assignment_question_list = ''
    assignment_from_url = ''

    try:
        course_from_url = db(db.course.url_title == request.args(0)).select()[0]

        create_new_assignment_form = SQLFORM(db.assignment)
        if create_new_assignment_form.process(formname='create_new_assignment_form').accepted:           
            db(db.assignment.id==create_new_assignment_form.vars.id).update(course_id=course_from_url['id'])
            session.flash = 'Assignment Created'
            redirect(URL('/course/' + course_from_url['url_title'] + '/assignments'))
        elif create_new_assignment_form.errors:
            session.flash = 'Error' 
            redirect(URL(''))

        create_new_page_form = SQLFORM(db.course_page)
        if create_new_page_form.process(formname='create_new_page_form').accepted:           
            db(db.course_page.id==create_new_page_form.vars.id).update(course_id=course_from_url['id'])
            session.flash = 'Page Created'
            redirect(URL('/course/' + course_from_url['url_title'] + '/pages'))
        elif create_new_page_form.errors:
            session.flash = 'Error' 
            redirect(URL(''))
        if request.args(1) == 'assignment':
            if request.args(2) is not None:
                assignment_from_url = db(db.assignment.id == request.args(2)).select()[0]
                form_create_question = SQLFORM(db.assignment_question)
                if form_create_question.process(formname='form_create_question').accepted:           
                    db(db.assignment_question.id==form_create_question.vars.id).update(assignment_id=assignment_from_url['id'])
                    session.flash = 'Question Created'
                    redirect(URL('/course/' + course_from_url['url_title'] + '/assignment/' + assignment_from_url['id'] + '/'))
                elif form_create_question.errors:
                    session.flash = 'Error' 
                    redirect(URL(''))
                assignment_question_list = db(db.assignment_question.assignment_id == assignment_from_url['id']).select()
        assignment_list = db(db.assignment.course_id == course_from_url['id']).select()
        page_list = db(db.course_page.course_id == course_from_url['id']).select()

        course_member_list = db(db.course_member.course_id == course_from_url['id']).select()

    except IndexError:
        redirect(URL('courses'))
    
    
    return dict(
        course_from_url=course_from_url,
        create_new_assignment_form=create_new_assignment_form,
        assignment_list=assignment_list,
        form_create_question=form_create_question,
        assignment_question_list=assignment_question_list,
        assignment_from_url=assignment_from_url,
        create_new_page_form=create_new_page_form,
        page_list = page_list,
        course_member_list=course_member_list,

    )
   

################################
####courses#####################
################################        
def courses():

    course_list = db(db.course).select()
    course_tag_list = db(db.course_tag).select()
    academy_list = db(db.academy).select().as_list() 

    return dict(
        academy_list=academy_list,
        course_list=course_list,
        course_tag_list=course_tag_list,
    )            


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

    import random
    academy_list = db(db.academy).select().as_list() 
    random.shuffle(academy_list)
    academy_list = academy_list[0:5]

    course_list = db(db.course).select().as_list() 
    random.shuffle(course_list)
    course_list = course_list[0:5]

    thread_list = db(db.thread).select().as_list() 
    random.shuffle(thread_list)
    thread_list = thread_list[0:5]
   
    return dict(
        academy_list=academy_list,
        course_list=course_list,
        thread_list=thread_list,
    )

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
        id_from_url = db(db.auth_user.username == request.args(0)).select()[0]['id']
        #courses_distributed = db(db.auth_user.id == db.course.creator_id).select()
        #courses_distributed_num = len(courses_distributed)
        courses = db(db.course_member.member_id == id_from_url).select()
      
    except IndexError:
        redirect(URL('members'))
    
    
    return dict(
        username_from_url=username_from_url, 
        courses = courses,
    )
    
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
    academy_list = db(db.academy).select().as_list() 
    course_list = db(db.course).select().as_list() 

    return dict(
        academy_list=academy_list,
        course_list=course_list,
    )
    

################################################################
####ajax########################################################
################################################################   

def academies_post():
    form=SQLFORM(db.academy)
    if form.accepts(request, formname=None):
        return DIV("Message posted")
    elif form.errors:
        return TABLE(*[TR(k, v) for k, v in form.errors.items()])

def courses_post():
    form=SQLFORM(db.course)
    if form.accepts(request, formname=None):
        return DIV("Message posted")
    elif form.errors:
        return TABLE(*[TR(k, v) for k, v in form.errors.items()])




################################
####ajax_join_academy###########
################################                     
def ajax_join_academy():
    academy_id = request.vars.itervalues()
    for x in academy_id:
        academy_id_trim = int(x)
        
    #LOGIC
    db.academy_member.insert(member_id = auth.user_id, academy_id = academy_id_trim, academy_membergroup_id_array=1)
    jquery = "jQuery('.flash').html('joined academy').slideDown().delay(1000).slideUp();"

    #jquery += "$('#join-collection-%s').fadeToggle(100);" % collection_id_trim
    #jquery += "$('#leave-collection-%s').delay(100).fadeToggle(400);" % collection_id_trim   
    return jquery      
    
################################
####ajax_leave_academy##########
################################     
def ajax_leave_academy():
    academy_id = request.vars.itervalues()
    for x in academy_id:
        academy_id_trim = int(x)

    #LOGIC
    db((db.academy_member.member_id==auth.user_id) & (db.academy_member.collection_id==academy_id_trim)).delete()
    jquery = "jQuery('.flash').html('left academy').slideDown().delay(1000).slideUp();"

    #jquery += "$('#leave-collection-%s').fadeToggle(100);" % collection_id_trim
    #jquery += "$('#join-collection-%s').delay(100).fadeToggle(400);" % collection_id_trim   
    return jquery
       

################################
####ajax_join_course############
################################                     
def ajax_join_course():
    course_id = request.vars.itervalues()
    for x in course_id:
        course_id_trim = int(x)
        
    #LOGIC
    db.course_member.insert(member_id = auth.user_id, course_id = course_id_trim, course_membergroup_id_array=1)
    jquery = "jQuery('.flash').html('joined course').slideDown().delay(1000).slideUp();"

    #jquery += "$('#join-collection-%s').fadeToggle(100);" % collection_id_trim
    #jquery += "$('#leave-collection-%s').delay(100).fadeToggle(400);" % collection_id_trim   
    return jquery      
    
################################
####ajax_leave_course###########
################################     
def ajax_leave_course():
    course_id = request.vars.itervalues()
    for x in course_id:
        course_id_trim = int(x)

    #LOGIC
    db((db.course_member.member_id==auth.user_id) & (db.course_member.collection_id==course_id_trim)).delete()
    jquery = "jQuery('.flash').html('left course').slideDown().delay(1000).slideUp();"

    #jquery += "$('#leave-collection-%s').fadeToggle(100);" % collection_id_trim
    #jquery += "$('#join-collection-%s').delay(100).fadeToggle(400);" % collection_id_trim   
    return jquery



            
################################################################
####helpers#####################################################
################################################################

################################
####download####################
################################   
@cache.action()
def download():
    return response.download(request, db)

################################
####call########################
################################ 
@auth.requires_login()
def call():
    return service()

################################
####data########################
################################ 
@auth.requires_signature()
def data():
    return dict(form=crud())

@service.xmlrpc
def test_add(a,b):
    number_sum = a+b
    return a+b

def Login():
    return "Not logged in";





