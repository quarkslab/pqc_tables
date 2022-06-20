//
//  Inspired by the different PQCgenKAT_sign.c
//
//  Created by Bassham, Lawrence E (Fed) on 8/29/17.
//  Copyright © 2017 Bassham, Lawrence E (Fed). All rights reserved.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
RNG
#include "api.h"

#define SUCCESS                    0
#define KEYPAIR                    1
#define SIGN                       2
#define SIGN_LENGTH                4
#define SIGN_OPEN                  8
#define SIGN_OPEN_MESSAGE_LENGTH  16
#define SIGN_OPEN_MESSAGE         32
#define ENTRY_FAILURE            -1

void fprintBstr(FILE *fp, char *S, unsigned char *A, unsigned long long L) {
	unsigned long long  i;

	fprintf(fp, "%s", S);

	for (i = 0; i < L; i++)
		fprintf(fp, "%02x", A[i]);

	if (L == 0)
		fprintf(fp, "00");

	fprintf(fp, "\n");
}

void readhex(unsigned char * m, unsigned long long mlen, char * str) {
  for (unsigned long long i = 0; i < mlen; i++)
    sscanf(str + 2 * i, "%2x", (unsigned int *) (m + i));
}

int main(int argc, char ** argv) {
  fprintf(stdout, "sklen = %u\n", CRYPTO_SECRETKEYBYTES);
  fprintf(stdout, "pklen = %u\n", CRYPTO_PUBLICKEYBYTES);
  fprintf(stdout, "sglen = %u\n", CRYPTO_BYTES);
  int                ret = SUCCESS;

#if 0
  unsigned char entropy_input[48];

  if (argc == 2) {
    for (int i = 0; i < 48; i++)
      entropy_input[i] = i;

  } else if (argc == 3) {
    if (strlen(argv[2]) != 96) {
      fprintf(stderr, "entropy input: expected 48 bytes, got <%ld>\n", strlen(argv[2]) / 2);
      return ENTRY_FAILURE;
    }

    readhex(entropy_input, 48, argv[2]);
  } else {
    return ENTRY_FAILURE;
  }

  unsigned char      *m,   *sm,   *m1;
  unsigned long long mlen, smlen, m1len;
  unsigned char      pk[CRYPTO_PUBLICKEYBYTES], sk[CRYPTO_SECRETKEYBYTES];
  int                ret_val;

  RANDOMBYTES_INIT

  mlen = strlen(argv[1]) / 2;
  m = (unsigned char *) malloc(mlen * sizeof(unsigned char));
  readhex(m, mlen, argv[1]);

  /*fprintBstr(stdout, "msg = ", m, mlen);*/

  m1 = (unsigned char *)calloc(mlen,              sizeof(unsigned char));
  sm = (unsigned char *)calloc(mlen+CRYPTO_BYTES, sizeof(unsigned char));

  // Generate the public/private keypair
  if ((ret_val = crypto_sign_keypair(pk, sk)) != 0) {
    fprintf(stderr, "crypto_sign_keypair returned <%d>\n", ret_val);
    ret |= KEYPAIR;
  }
  /*fprintBstr(stdout, "pk = ", pk, CRYPTO_PUBLICKEYBYTES);*/
  /*fprintBstr(stdout, "sk = ", sk, CRYPTO_SECRETKEYBYTES);*/
  
  if ((ret_val = crypto_sign(sm, &smlen, m, mlen, sk)) != 0) {
    fprintf(stderr, "crypto_sign returned <%d>\n", ret_val);
    ret |= SIGN;
  }
  /*fprintBstr(stdout, "sm = ", sm, smlen);*/

  // smlen is larger than expected
  if (CRYPTO_BYTES + mlen < smlen) {
    fprintf(stderr, "crypto_sign returned bad 'sglen': got <%llu>, expected <%llu>\n", smlen - mlen, (unsigned long long) CRYPTO_BYTES);
    ret |= SIGN_LENGTH;
  }

  // smlen is smaller than expected
  if (CRYPTO_BYTES + mlen > smlen) {
    fprintf(stderr, "crypto_sign returned smallest 'sglen': got <%llu>, expected <%llu>\n", smlen - mlen, (unsigned long long) CRYPTO_BYTES);
  }

  if ((ret_val = crypto_sign_open(m1, &m1len, sm, smlen, pk)) != 0) {
    fprintf(stderr, "crypto_sign_open returned <%d>\n", ret_val);
    ret |= SIGN_OPEN;
  }
  
  if (mlen != m1len) {
    fprintf(stderr, "crypto_sign_open returned bad 'mlen': got <%llu>, expected <%llu>\n", m1len, mlen);
    ret |= SIGN_OPEN_MESSAGE_LENGTH;
  }
  
  if (memcmp(m, m1, mlen)) {
    fprintf(stderr, "crypto_sign_open returned bad 'm' value\n");
    return SIGN_OPEN_MESSAGE;
  }
 
  free(m);  
  free(m1);
  free(sm);

#endif // 0
       //
  return ret;
}
