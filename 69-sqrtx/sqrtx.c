int mySqrt(int x) {
  	long int i;
    long int a=0;
		for(i=0;i<=x;i++)
	{
	
	if(i*i>x)
	break;
	else if(i*i<=x)
	{

		a=i;
		continue;
		
	}
	else if(i*i==x)
	{
	return i;
	break;
	}
	
	}
return a;}