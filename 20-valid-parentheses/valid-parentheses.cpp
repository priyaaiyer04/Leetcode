class Solution {
public:
    bool isValid(string s) {
      stack<char> st;
      int c1=0,c2=0,c3=0,c4=0,c5=0,c=0;
    for(char i:s)
    {
        if (i=='(')
        {
            c1++;
        }
        if (i==')')
        {
          c2++;
        }
        if (i=='[')
        {
           c3++;
        }
           if (i==']')
        {
            c4++;
        }
        if (i=='{')
        {c5++;
        }
        if (i=='}')
        {c++;
        }
    }  
   
    if(s.length()%2==0 and c1==c2 and c3==c4 and c5==c){
    for(char i:s)
    {
        if (i=='(')
        {
            st.push(i);
        }
        if (i=='{')
        {
            st.push(i);
        }
        if (i=='[')
        {
            
            st.push(i);
        }
           if (i==')')
        {
            if (!st.empty() && st.top()=='(')
            st.pop();
        }
        if (i=='}')
        {if (!st.empty() && st.top()=='{')
            st.pop();
        }
        if (i==']')
        {
           if (!st.empty() && st.top()=='[')
            st.pop();
        }
    }
    if (st.empty())
    return 1;
    else
    return 0;  
    }
       
  return 0;  
}};