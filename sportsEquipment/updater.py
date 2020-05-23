# from .models import *
# from login.forms import UserForm,UserProfileInfoForm
# from login.models import UserProfileInfo
# from pytz import timezone
# from datetime import *

# def utcToIst(lstRequest):
#     for request in lstRequest:
#         if request.dtOfRequest is not None:
#             request.dtOfRequest = request.dtOfRequest.astimezone(timezone('Asia/Kolkata'))
#         if request.dtOfExpRet is not None:
#             request.dtOfExpRet = request.dtOfExpRet.astimezone(timezone('Asia/Kolkata'))
#         if request.dtOfActualRet is not None:
#             request.dtOfActualRet = request.dtOfActualRet.astimezone(timezone('Asia/Kolkata'))
#         if request.dtAvailed is not None:
#             request.dtAvailed = request.dtAvailed.astimezone(timezone('Asia/Kolkata'))

#     return lstRequest

# def update_penalty():
#     lstProcessedRequest = list(EquipmentRequest.objects.filter(reqStatus__in = [1]).order_by('-dtOfRequest'))
#     lstProcessedRequest = utcToIst(lstProcessedRequest)
#     print(lstProcessedRequest)
#     print("No of processed requests: ", len(lstProcessedRequest))
#     return
#     #return render(request, 'AdminUser/processedRequest.html', {'lstProcessedRequest': lstProcessedRequest,'userProfile': userProfile});