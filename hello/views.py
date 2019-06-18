from django.shortcuts import render
from django.http import HttpResponse
from .forms import IntForm

#bit length
def bit_length(x):
    k = 1
    cnt = 0
    while k < x:
        k = k << 1
        cnt += 1
    return cnt

#n以下の素数列挙(O(n log(n))
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    res = '(len:'+str(len(ass))+') >>'
    for e in ass:
        res += str(e) + ' '
    return res


def index(request):
    params = {
            'title' : 'number info',
            'message' : 'input num: ',
            'form' : IntForm()
            }
    
    if (request.method == 'POST'):
        input_num = int(request.POST['input_num'])

        params['message'] = 'input num: ' + str(input_num) + \
        '<br> primes: ' + primes(input_num) + \
        '<br> 2^' + str(bit_length(input_num)) + ' <= '+ str(input_num) + ' < 2^' + str(bit_length(input_num)+1)
        params['form'] = IntForm(request.POST)
    return render(request,'hello/index.html',params)

