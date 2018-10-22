def creditAAoAIncreaseStrategy( annualApplicationCount, initialCreditWait, numberOfYears ):
	int_format_str = '{:2d}';
	float_format_str = '{:8.4f}';
	i = 1.0;
	step = 1.0 / float(annualApplicationCount);
	temp = float(initialCreditWait);
	while ( i < annualApplicationCount * numberOfYears ):
		newTemp = ( temp + step ) * i / ( i + 1.0 );
		i = i + 1.0;
		print( "Year ", int_format_str.format( int( i / annualApplicationCount) ) ,
		 " Application ", int_format_str.format( int( i % int(annualApplicationCount) + 1 ) ) ,
		 " | Average Age of Accounts = ", float_format_str.format( newTemp ) ,
         " years  -  efficiency = ", float_format_str.format( (newTemp-temp)*100/step ), "%  |  Total Age of Accounts = ",
          float_format_str.format( newTemp * i ) + " years  |  Count of Accounts = ", int(i) );
		temp = newTemp;

creditAAoAIncreaseStrategy( 2.0, 1.0, 25 );
input("Press any key to continue...");
