from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentGradeSchema, AssignmentSchema

teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)

# List all the assignmnet associated with teacher 
@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False) #
@decorators.auth_principal
def list_assignments(p):
    """Returns list of assignments submitted to teacher"""
    teacher_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)   #
    teachers_assignments_dump = AssignmentSchema().dump(teacher_assignments, many=True) #
    return APIResponse.respond(data=teachers_assignments_dump)  #


# Teacher graded the assignment
@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)  #
@decorators.accept_payload
@decorators.auth_principal
def grade_assignment(p, incoming_payload):  
    """Grade an assignment"""

    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    # print(f" grade => {grade_assignment_payload.grade}")

    gradded_assignment = Assignment.graded( 
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(gradded_assignment)    #
    return APIResponse.respond(data=graded_assignment_dump)     #
