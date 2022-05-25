def dummy():
   return 45

def foo():
    print('bar!')
    return 1
          
public_data = "public stuff!"
_private_data = "private stuff!"

if __name__ == '__main__':
    # test dummy
    if dummy() == 45:
       print('success')
    if foo() == 1:
       print('success 2')
    
