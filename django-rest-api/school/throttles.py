from rest_framework.throttling import AnonRateThrottle

class EnrollmentAnonThrottle(AnonRateThrottle):
    rate = '5/day'    