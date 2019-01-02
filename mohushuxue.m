clc;
clear;
A=[1 0.6 0.5 0.7 0;0.4 1 0.7 0.9 0.2;0.6 0.6 1 0.5  0;0.5 0.7 0.9 1 0.6;0.8 0 0.7 0.9 1];
[m,n]=size(A);
a=[];
for i=1:1
    for j=1:1
        
        for p=1:m
            for q=1:n
                if  A(q,p)>=A(p,q)
                    a(q,p)=A(p,q);
                    if p==2
                        break
                    end
                else
                    a(q,p)=A(q,p);
                end
               a(q,p)
                
             end
        end
        a
        
    end
end