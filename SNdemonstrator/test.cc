#include <iostream>
#include <cmath>

using namespace std;


int main(){

  double tau_sc=2.5;
  double fwhm_tts=2.25;
  double factor=2*sqrt(2*log(2));
  double fwhm_E=0.08;

  double N_pe=pow((factor/fwhm_E),2);

  double sigma_t=sqrt((pow(tau_sc,2)+pow(fwhm_tts,2)/factor)/N_pe);

  cout << N_pe << endl ;
  cout << sigma_t << endl ;

}
