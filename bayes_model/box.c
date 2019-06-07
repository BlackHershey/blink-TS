//
//  box.c
//  
//
//  Created by Haley Botteron on 3/5/18.
//
//

#include <stdio.h>
#include <math.h>

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
    double base, top, t_i;
    
    base = Params[0];
    top = Params[1];
    
    for (CurEntry = 0; CurEntry < *TotalDataValues; CurEntry++)
    {
        tindex = 2*CurEntry;
        t_i = Abscissa[tindex];
        
        if (t_i < 60.0 ) {
            Signal[CurEntry] = top;
        } else {
            Signal[CurEntry] = base;
        }
    }  // end for CurEntry
    
    return;
}
