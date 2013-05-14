
#总页数
def page(total,rows):
    page=0
    if total%rows==0:
            page=total/rows
    else:
            page=total/rows+1
    return int(page)





