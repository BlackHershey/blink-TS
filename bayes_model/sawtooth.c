
#include <stdio.h>
#include <math.h>
//
//  sawtooth.c
//
//
//  Created by Haley Botteron on 3/5/18.
//
//
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
    
    int CurEntry, tindex;
    double base, top,t_i;
    
    base = Params[0];
    top = Params[1];
    
    for (CurEntry = 0; CurEntry < *TotalDataValues; CurEntry++)
    {
        tindex = 2*CurEntry;
        t_i = Abscissa[tindex];
        
        if (t_i < 60.0 ) {
            Signal[CurEntry] = base + t_i * ( top - base ) / 60.;
        } else if (t_i <= 75.0 ) {
            Signal[CurEntry] = base + (t_i - 75.)*(top - base)/(60. - 75.);
        } else {
            Signal[CurEntry] = base;
        }
    }  // end for CurEntry

    return;
}
