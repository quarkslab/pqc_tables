PWD_entry=`pwd`
M=7934d3a580b1393e410c92e5c63fd7974cc3e42cb4733f0525b97b75c5a64fb4

# ------------------------------------------------------------------------------

# Dilithium
echo Dilithium

wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/Dilithium-Round3.zip
unzip -q Dilithium-Round3.zip

PATH_code=Dilithium/dilithium/Reference_Implementation/crypto_sign/dilithium5
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd $PATH_code
make > /dev/null 2>&1
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

# ------------------------------------------------------------------------------

# Falcon
echo Falcon

wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/Falcon-Round3.zip
unzip -q Falcon-Round3.zip

PATH_code=Falcon/falcon-round3/KAT/generator
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"katrng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd Falcon/falcon-round3/Reference_Implementation/falcon1024/falcon1024int
make > /dev/null 2>&1
cd build
./kat1024int $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

# ------------------------------------------------------------------------------

# Rainbow
echo Raimbow

wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/Rainbow-Round3.zip
unzip -q Rainbow-Round3.zip

PATH_code=Rainbow/Reference_Implementation
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd $PATH_code

echo Classic
cp Vc_Classic/rainbow_config.h Vc_Classic/rainbow_config.h.bak
sed -i "s/#define _V1 96/#define _V1 148/" Vc_Classic/rainbow_config.h
make PROJ_DIR=Vc_Classic > /dev/null 2>&1
./PQCgenKAT_sign $M
make clean > /dev/null 2>&1
cp Vc_Classic/rainbow_config.h.bak Vc_Classic/rainbow_config.h
rm Vc_Classic/rainbow_config.h.bak

echo Circumzenithal
cp Vc_Circumzenithal/rainbow_config.h Vc_Circumzenithal/rainbow_config.h.bak
sed -i "s/#define _V1 96/#define _V1 148/" Vc_Circumzenithal/rainbow_config.h
make PROJ_DIR=Vc_Circumzenithal > /dev/null 2>&1
./PQCgenKAT_sign $M
make clean > /dev/null 2>&1
cp Vc_Circumzenithal/rainbow_config.h.bak Vc_Circumzenithal/rainbow_config.h
rm Vc_Circumzenithal/rainbow_config.h.bak

echo Compressed
cp Vc_Compressed/rainbow_config.h Vc_Compressed/rainbow_config.h.bak 
sed -i "s/#define _V1 96/#define _V1 148/" Vc_Compressed/rainbow_config.h
make PROJ_DIR=Vc_Compressed > /dev/null 2>&1
./PQCgenKAT_sign $M
cp Vc_Compressed/rainbow_config.h.bak Vc_Compressed/rainbow_config.h
rm Vc_Compressed/rainbow_config.h.bak

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

# ------------------------------------------------------------------------------
# GeMSS

#wget https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/GeMSS-Round3.zip
#unzip GeMSS-Round3.zip

# TODO

# ------------------------------------------------------------------------------

# Picnic
echo Picnic

wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/Picnic-Round3.zip
unzip -q Picnic-Round3.zip

echo FS
PATH_code=picnic_submission_round3/Reference_Implementation/picnicl5fs/NIST-KATs
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/NIST_randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd picnic_submission_round3/Reference_Implementation/picnicl5fs
make nistkat > /dev/null 2>&1
cd NIST-KATs
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

echo Full
PATH_code=picnic_submission_round3/Reference_Implementation/picnicl5full/NIST-KATs
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/NIST_randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd picnic_submission_round3/Reference_Implementation/picnicl5full
make nistkat > /dev/null 2>&1
cd NIST-KATs
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

echo UR
PATH_code=picnic_submission_round3/Reference_Implementation/picnicl5ur/NIST-KATs
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/NIST_randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd picnic_submission_round3/Reference_Implementation/picnicl5ur
make nistkat > /dev/null 2>&1
cd NIST-KATs
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

echo Picnic3
PATH_code=picnic_submission_round3/Reference_Implementation/picnic3l5/NIST-KATs
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/NIST_randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd picnic_submission_round3/Reference_Implementation/picnic3l5
make nistkat > /dev/null 2>&1
cd NIST-KATs
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

cd $PWD_entry

# ------------------------------------------------------------------------------

# SPHINCS+
echo SPHINCS+

wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/SPHINCS-Round3.zip
unzip -q SPHINCS-Round3.zip

echo shake256-256f-simple
PATH_code=NIST-PQ-Submission-SPHINCS-20201001/Reference_Implementation/crypto_sign/sphincs-shake256-256f-simple
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd $PATH_code
make > /dev/null 2>&1
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

echo shake256-256f-robust
PATH_code=NIST-PQ-Submission-SPHINCS-20201001/Reference_Implementation/crypto_sign/sphincs-shake256-256f-robust
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd $PATH_code
make > /dev/null 2>&1
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

echo shake256-256s-simple
PATH_code=NIST-PQ-Submission-SPHINCS-20201001/Reference_Implementation/crypto_sign/sphincs-shake256-256s-simple
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd $PATH_code
make > /dev/null 2>&1
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

echo shake256-256s-robust
PATH_code=NIST-PQ-Submission-SPHINCS-20201001/Reference_Implementation/crypto_sign/sphincs-shake256-256s-robust
cp $PATH_code/PQCgenKAT_sign.c $PATH_code/PQCgenKAT_sign.c.bak
cp test_sig.c $PATH_code/PQCgenKAT_sign.c
sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_sign.c
sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_sign.c

cd $PATH_code
make > /dev/null 2>&1
./PQCgenKAT_sign $M

cd $PWD_entry
cp $PATH_code/PQCgenKAT_sign.c.bak $PATH_code/PQCgenKAT_sign.c
rm $PATH_code/PQCgenKAT_sign.c.bak

# ------------------------------------------------------------------------------

## Classic McEliece
#echo Classic McEliece

##wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/Classic-McEliece-Round3.zip
##unzip -q -d Classic-McEliece Classic-McEliece-Round3.zip

#TODO

# ------------------------------------------------------------------------------

## Kyber
#echo Kyber

##wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/Kyber-Round3.zip
##unzip -q Kyber-Round3.zip

#PATH_code=NIST-PQ-Submission-Kyber-20201001/Reference_Implementation/crypto_kem/kyber1024
#cp $PATH_code/PQCgenKAT_kem.c $PATH_code/PQCgenKAT_kem.c.bak
#cp test_kem.c $PATH_code/PQCgenKAT_kem.c
#sed -i "s/RNG/#include \"rng.h\"/" $PATH_code/PQCgenKAT_kem.c
#sed -i "s/RANDOMBYTES_INIT/randombytes_init(entropy_input, NULL, 256);/" $PATH_code/PQCgenKAT_kem.c

#cd $PATH_code
#make > /dev/null 2>&1
#./PQCgenKAT_kem

#cd $PWD_entry
#cp $PATH_code/PQCgenKAT_kem.c.bak $PATH_code/PQCgenKAT_kem.c
#rm $PATH_code/PQCgenKAT_kem.c.bak

# ------------------------------------------------------------------------------

## Frodo KEM
#echo Frodo KEM

#wget -q https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/FrodoKEM-Round3.zip
#unzip -q FrodoKEM-Round3.zip

#

## NTRU
#echo NTRU

#git clone https://github.com/jschanck/ntru.git


