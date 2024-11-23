from django.utils.deprecation import MiddlewareMixin

class UserRoleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            # Ensure user role consistency across sessions
            if not request.session.get('user_role'):
                request.session['user_role'] = request.user.current_role