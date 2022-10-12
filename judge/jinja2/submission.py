from . import registry


@registry.function
def submission_layout(
    submission, profile_id, user, editable_problem_ids, completed_problem_ids
):
    problem_id = submission.problem_id
    can_view = False

    if problem_id in editable_problem_ids:
        can_view = True

    if profile_id == submission.user_id:
        can_view = True

    if user.has_perm("judge.change_submission"):
        can_view = True

    if user.has_perm("judge.view_all_submission"):
        can_view = True

    if submission.problem.is_public and user.has_perm("judge.view_public_submission"):
        can_view = True

    if submission.problem_id in completed_problem_ids:
        can_view |= (
            submission.problem.is_public or profile_id in submission.problem.tester_ids
        )

    if not can_view and hasattr(submission, "contest"):
        contest = submission.contest.participation.contest
        if contest.is_editable_by(user):
            can_view = True

    return can_view
