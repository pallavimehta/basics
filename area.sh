read -p "Calculating of area of circle with radius : " radius

echo "Area =  $(echo "scale=5;(3.14 * $radius * $radius)" | bc)"

read -p "Calculating circumference of circle with diameter : " diameter

echo "Diameter = $(echo "scale=5;(3.14 * $diameter)" | bc)"

read -p "Interest on you loan. ROR is 4%. Enter Principal amt, term(in years)" Amt noyrs

echo "Intrest = $(echo "scale=5;(($Amt * $noyrs * 4)/100)" | bc)"

