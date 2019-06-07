#include <stdio.h>
#include <math.h>

// Kevin added the “if t<60” stuff, 02 Aug 2017

void model_(int *CurSet,
	int *NoOfParams,
	int *NoOfDerived,
	int *TotalDataValues,
	int *MaxNoOfDataValues,
	int *NoOfDataCols,
	int *NoOfAbscissaCols,
	int *NoOfModelVectors,
	double  Params[],
	double  Derived[],
	double  Abscissa[],
	double  Signal[]){

	int CurEntry, tindex, j;
	double a, b, c, k, h, t_i, t_delta, Hij, f_j, eye_closure_sum, term1, term2, term3, previous_term3, r;

	a = Params[0];
	b = Params[1];
	c = Params[2];
	k = Params[3];
	h = Params[4];
    r = Params[5];

	for (CurEntry = 0; CurEntry < *TotalDataValues; CurEntry++)
	{
		tindex = 2*CurEntry;
		t_i = Abscissa[tindex];

		// first model term
        if ( t_i < c ) {
            term1 = 0;
        } else {
            term1 = a*sqrt(t_i - c);
        } // intent is to use a>0 and 0 <= c <= 20

		// second model term
		term2 = b;

		if ( CurEntry == 0 ){
			term3 = 0;
		} else {
			previous_term3 = term3;

			// sum over j < i
			eye_closure_sum = 0.0;
			for (j = 0; j < CurEntry; j++){
				t_delta = t_i - Abscissa[2*j];
				f_j = Abscissa[2*j + 1];
				if ( f_j > 0 && t_delta <= 2*h ){
					Hij = (t_delta*(2*h-t_delta))/pow(h,2);
					eye_closure_sum += f_j*Hij;
				}
			}
			// third model term
			term3 = k*eye_closure_sum;
		}

		if ( t_i <= 60.0 ){
			Signal[CurEntry] = term1 + term2 + term3;
		} else {
			// see email from Kevin 23 Oct 2017
			// Decrease D by a rate proportional to the distance back to baseline ...
			// ... with rate constant r if eyes were closed the whole previous quarter second,
			// but with rate a fraction of r if eyes were closed less than that. Namely:
			// ΔD = Δt * [frac.] * (-r) * [D(t-1) - b]
            // oops, "f_j" below should be Abscissa[2*(CurEntry-1)+1], but yay, it is
			Signal[CurEntry] = Signal[CurEntry-1] + t_delta*f_j*(-r)*(Signal[CurEntry-1]-b);
		}
		
	}

	return;
}
