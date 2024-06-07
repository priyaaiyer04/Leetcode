class Solution {
public:
    string defangIPaddr(string address) {
        int d=address.length();
for(int i=0;i<d;i++)
{
	if (address[i]=='.')
	{ 
	address.replace(i,1,"[.]");
d+=3;
i+=3;

}
   
   
}
return address;
    }
};