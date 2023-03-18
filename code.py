class Solution:
    def isRectangleCover(self, rectangles):
        a,b,c,d,e,f=float('inf'),float('inf'),float('-inf'),float('-inf'),0,set() # x1 , y1 , x2 , y2 , e -> area ,f->corner 
        for g,h,i,j in rectangles:
            a,b,c,d,e=min(a,g),min(b,h),max(c,i),max(d,j),e+(i-g)*(j-h)
            f^={(g,h),(i,j),(g,j),(i,h)}
        return f=={(a,b),(c,d),(a,d),(c,b)} and e==(c-a)*(d-b)
