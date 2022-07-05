# PQC tables

The goal of the following tables is to summarize the current [ANSSI](#ANSSI) views regarding post-quantum cryptography scheme usages for (French) certifications. These tables are subject to change depending on new cryptanalysis, new submitted algorithms to the [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography), new recommandations, etc. The simplified tables may give a quick overview of the ANSSI recommandations, while the larger tables will give more information, in particular about the sizes of the private key (sk), the public key (pk), the ciphertext (ct), the shared secret (ss) and the signature (sig).

## Tables (simplified)

### On the ANSSI column

According to [[ANSSI](#ANSSI)],

> Moreover the conjectured post-quantum level should be as high as possible, preferably NIST level V (AES-256).

> ANSSI encourages to use a conjectured post-quantum security level on symmetric primitives consistent with the selected post-quantum PKC algorithm – in practice at least the same security level as AES-256 for block ciphers and at least the same security level as SHA2-384 for hash functions.

We then consider, in the ANSSI column, that if a cryptographic scheme does not provide security parameters for level IV (at least as hard to break as SHA2-384) or level V (at least as hard to break as AES-256), the scheme is not suitable to be used to get a (French) certification.

About the hybrid mechanism, it can be:

* *concatenate KDF* for key exchange mechanisms, see Section 3.3 of [[SFG](#SFG)] or Section 8.2 of [[ETSI](#ETSI)];
* *cascade KDF* for key exchange mechanisms, see Section 8.3 of [[ETSI](#ETSI)];
* *concatenate* for signatures.

### Notes (simplified tables)

We give in notes some additional content, either to justify our results or to give more information and some recommendations, coming from the ANSSI views or from other governments’ positions. Indeed, as mentioned in [ANSSI](#ANSSI),

> Several governments have published similar position papers recommending to prepare the post-quantum transition. ANSSI’s views are similar to the BSI’s position on many issues (e.g. necessary migration, hybridation, cryptoagility).

Even if these tables are focused on the French context, they may be used in other national contexts too.

### Post-quantum cryptography key exchange mechanisms and their usage for (French) certifications (simplified tables)

| KEM                                                         | Variants (best security level)               | NIST                            | ANSSI   [[ANSSI](#ANSSI)] |
| ---                                                         | ---                                          | ---                             | ---                       |
| [Classic McEliece](https://classic.mceliece.org/)           | 6688128(f), 6960119(f), 8192128(f)           | Finalist (round 3)  [[22](#22)] | Hybrid          [[7](#7)] |
| [CRYSTALS-KYBER](https://pq-crystals.org/kyber/index.shtml) | 1024                                         | Finalist (round 3)  [[22](#22)] | Hybrid        [[13](#13)] |
| [NTRU](https://ntru.org/)                                   | HPS-4096-821                                 | Finalist (round 3)  [[22](#22)] | Maybe hybrid    [[1](#1)] |
| [NTRU](https://ntru.org/)                                   | HPS-4096-1229, HRSS-1373           [[2](#2)] | Finalist (round 3)  [[22](#22)] | Hybrid                    |
| [SABER](https://www.esat.kuleuven.be/cosic/pqcrypto/saber/) | (u)FireSaber                                 | Finalist (round 3)  [[22](#22)] | Hybrid                    |
| [BIKE](https://bikesuite.org/)                              | Level 5                                      | Alternate (round 3) [[22](#22)] | Hybrid                    |
| [FrodoKEM](http://frodokem.org/)                            | 1344                                         | Alternate (round 3) [[22](#22)] | Hybrid          [[8](#8)] |
| [HQC](http://pqc-hqc.org/)                                  | 256                                          | Alternate (round 3) [[22](#22)] | Hybrid                    |
| [NTRU Prime](https://ntruprime.cr.yp.to/)                   | sntrup1277, ntrulpr1277                      | Alternate (round 3) [[22](#22)] | Hybrid                    |
| [SIKE](http://sike.org/)                                    | p751                                         | Alternate (round 3) [[22](#22)] | Hybrid                    |

### Post-quantum cryptography signatures and their usage for (French) certifications (simplified tables)

| Signature                                                           | Variants (best security level)                | NIST                            | ANSSI   [[ANSSI](#ANSSI)] |
| ---                                                                 | ---                                           | ---                             | ---                       |
| Stateful hash-based                                                 | [LMS, HSS](https://datatracker.ietf.org/doc/html/rfc8554), [XMSS, XMSS-MT](https://datatracker.ietf.org/doc/html/rfc8391) | Standard            [[10](#10)] | Compliant       [[9](#9)] |
| [CRYSTALS-DILITHIUM](https://pq-crystals.org/dilithium/index.shtml) | 5                                             | Finalist (round 3)  [[22](#22)] | Hybrid        [[13](#13)] |
| [FALCON](https://falcon-sign.info/)                                 | 1024                                          | Finalist (round 3)  [[22](#22)] | Hybrid        [[13](#13)] |
| [Rainbow](https://www.pqcrainbow.org/)                              | UOV parameters SL5                 [[6](#6)]  | Finalist (round 3)  [[22](#22)] | Hybrid                    |
| [GeMSS](https://www-polsys.lip6.fr/Links/NIST/GeMSS.html)           | 256, all variants                             | Alternate (round 3) [[22](#22)] | Not compliant [[15](#15)] |
| [Picnic](https://microsoft.github.io/Picnic/)                       | L5-FS, L5-UR, L5-full, 3-L5                   | Alternate (round 3) [[22](#22)] | Hybrid                    |
| [SPHINCS+](https://sphincs.org/)                                    | SHAKE-256s, SHA2-256s, SHAKE-256f, SHA2-256s  | Alternate (round 3) [[22](#22)] | Compliant       [[9](#9)] |

## Tables

### Notes

When two values are in a same cell, first is the one from the documentation, the second from the reference implementation submitted to [Round 3 submission of NIST Post-Quantum Cryptography](https://csrc.nist.gov/Projects/post-quantum-cryptography/round-3-submissions).

Other tables gathering data on PQC schemes can be found, for example at:

* [Algorithms in liboqs](https://openquantumsafe.org/liboqs/algorithms/);
* [[ETSIKEM](#ETSIKEM)] and [[ETSISIG](#ETSISIG)];
* [PQC wiki](https://pqc-wiki.fau.edu/w/Special:DatabaseHome).

It is also possible to look for the different `api.h` or `META.yml` of [PQClean](https://github.com/PQClean/PQClean).

For performance benchmarks, an interested reader may refer to [eBACS](https://bench.cr.yp.to/ebats.html) or [pqm4](https://github.com/mupq/pqm4).

In the variants of LMS, HSS, XMSS and XMSS-MT, the `..` or `../..` refers to the paramaters given:

* for LMS, in Table 2 of [[RFC8554](#RFC8554)];
* for XMSS, in Table 2 of [[RFC8391](#RFC8391)];
* for XMSS-MT, in Table 4 of [[RFC8391](#RFC8391)].

## Explanations

<a name="ANSSI">[ANSSI]</a> [ANSSI views on the Post-Quantum Cryptography transition](https://www.ssi.gouv.fr/publication/anssi-views-on-the-post-quantum-cryptography-transition/), 4 January 2022

<a name="BBCPSTV">[BBCPSTV]</a> J. Baena, P. Briaud, D. Cabarcas, R. Perlner, D. Smith-Tone and J. Verbel, [Improving Support-Minors rank attacks: applications to GeMSS and Rainbow](https://eprint.iacr.org/2021/1677.pdf) 

<a name="Beu">[Beu]</a> W. Beullens, [Breaking Rainbow Takes a Weekend on a Laptop](https://eprint.iacr.org/2022/214.pdf)

<a name="BSI">[BSI]</a> [Migration zu Post-Quanten-Kryptografie](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Krypto/Post-Quanten-Kryptografie.html), 24 August 2020; [Cryptographic Mechanisms: Recommendations and Key Lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.html), BSI TR-02102-1, Version: 2022-1, 11 February 2022

<a name="ETSI">[ETSI]</a> [Quantum-safe hybrid key exchanges](https://www.etsi.org/deliver/etsi_ts/103700_103799/103744/01.01.01_60/ts_103744v010101p.pdf). ETSI TS 103 744 V1.1.1, December 2020

<a name="ETSIKEM">[ETSIKEM]</a> [Quantum-Safe Public-Key Encryption and Key Encapsulation](https://www.etsi.org/deliver/etsi_tr/103800_103899/103823/01.01.01_60/tr_103823v010101p.pdf), ETSI TR 103 823, version 1.1.1, September 2021

<a name="ETSISIG">[ETSISIG]</a> [Quantum-Safe Signatures](https://www.etsi.org/deliver/etsi_tr/103600_103699/103616/01.01.01_60/tr_103616v010101p.pdf), ETSI TR 103 616, version 1.1.1, September 2021

<a name="KF">[KF]</a> P. Kampanakis and S. Fluhrer, [LMS vs XMSS: Comparion of two Hash-Based Signature Standards](https://eprint.iacr.org/2017/349)

<a name="KPCSA">[KPCSA]</a> P. Kampanakis, P. Panburana, M. Curcio, C. Shroff and M. M. Alam, [Post-Quantum LMS and SPHINCS+ Hash-Based Signatures for UEFI Secure Boot](https://eprint.iacr.org/2021/041.pdf)

<a name="NIST2020">[NIST2020]</a> G. Alagic, J. Alperin-Sheriff, D. Apon, D. Cooper, Q. Dang, J. Kelsey, Y.-K. Liu, C. Miller, D. Moody, R. Peralta, R. Perlner, A. Robinson and D. Smith-Tone, [Status Report on the Second Round of the NIST Post-Quantum Cryptography Standardization Process](https://csrc.nist.gov/publications/detail/nistir/8309/final), NISTIR 8309, July 2020

<a name="NISTSTD">[NISTSTD]</a> D. Cooper, D. Apon, Q. Dang, M. Davidson, M. Dworkin, and C. Miller, [Recommendation for Stateful Hash-Based Signature Schemes](https://doi.org/10.6028/NIST.SP.800-208), NIST Special Publication 800-208, October 2020

<a name="NLNCSA">[NLNCSA]</a> [Prepare for the threat of quantum-computers](https://english.aivd.nl/publications/publications/2022/01/18/prepare-for-the-threat-of-quantumcomputers), 18 January 2022 

<a name="RFC8391">[RFC8391]</a> A. Huelsing, D. Butin, S. Gazdag, J. Rijneveld and A. Mohaisen, [XMSS: eXtended Merkle Signature Scheme](https://datatracker.ietf.org/doc/html/rfc8391), RFC 8391, May 2018

<a name="RFC8554">[RFC8554]</a> D. McGrew, M. Curcio and S. Fluhrer, [Leighton-Micali Hash-Based Signatures](https://datatracker.ietf.org/doc/html/rfc8554), RFC8554, April 2019

<a name="SFG">[SFG]</a> D. Stebila, S. Fluhrer and S. Gueron, [Hybrid key exchange in TLS 1.3](https://datatracker.ietf.org/doc/html/draft-ietf-tls-hybrid-design-04), Network Working Group, Internet-Draft, 11 January 2022

<a name="TPD">[TPD]</a> C. Tao, A. Petzoldt and J. Ding, [Efficient Key Recovery for All HFE Signature Variants](https://doi.org/10.1007/978-3-030-84242-0_4). In: T. Malkin and C. Peikert (eds), CRYPTO 2021. LNCS, vol. 12825, pp. 70-93. Springer (11 August 2021)

<a name="1">[1]</a> Not compliant if conservative choice (non-local) for the computational model, hybrid otherwise

<a name="2">[2]</a> [Category 5 NTRU parameters](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/t1JCgzSS-uk/m/H9M8jdQDCQAJ)

<a name="3">[3]</a> I & III (non-local), I & III & V (local), not taking into account the parameters in [[2](#2)]

<a name="4">[4]</a> I (non-local), III (local), not taking into account the parameters in [[2](#2)]

<a name="5">[5]</a> Only from the code

<a name="6">[6]</a> After the attack in [[Beu](#Beu)] acknowledged in [ROUND 3 OFFICIAL COMMENT: Rainbow](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/KFgw5_qCXiI/m/cr66AGOfAgAJ), the authors proposed a new set of parameters [UOV parameters](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/B1RFy31rH8I/m/yIqAt7dABAAJ)

<a name="7">[7]</a> From [[BSI](#BSI)]

> The mechanisms FrodoKEM-976, FrodoKEM-1344 as well as **Classic McEliece** with the parameters in **Categories 3 and 5** are assessed to be cryptographically suitable to protect confidential.

From [[NLNCSA](#NLNCSA)]

> For PQC, we recommend the most secure algorithms, such as Frodo or **McEliece**.

<a name="8">[8]</a> From [[ANSSI](#ANSSI)]

> For example, a developer should be able to obtain a security visa for a product implementing FrodoKEM whether NIST decides that FrodoKEM will be one of the first PQC standards or not.

From [[BSI](#BSI)]

> The mechanisms FrodoKEM-976, **FrodoKEM-1344** as well as Classic McEliece with the parameters in Categories 3 and 5 are assessed to be cryptographically suitable to protect confidential.

From [[NLNCSA](#NLNCSA)]

> For PQC, we recommend the most secure algorithms, such as **Frodo** or McEliece.

<a name="9">[9]</a> From [[ANSSI](#ANSSI)]

> Hash-based signatures are an exception for hybridation: due to their well-studied underlying mathematical problem, ANSSI estimates that these algorithms could be used today without hybridation. However, their potential application range is limited (low number of signatures queries or large signature sizes).

<a name="10">[10]</a> See [[NISTSTD](#NISTSTD)], [[RFC8391](#RFC8391)] and [[RFC8554](#RFC8554)]

<a name="11">[11]</a> See Table 2 in [[KF](#KF)]

<a name="12">[12]</a> Only from the documentation

<a name="13">[13]</a> From [[ANSSI](#ANSSI)]

> For example, at the time of the writing, the NIST candidates FrodoKEM, **Kyber, Dilithium or Falcon** could be good options for first deployments.

<a name="14">[14]</a> Depending on the analysis of the security level (bulletproofing strategies), the security level is:

* IV (strategy #1) and may be used in a hybrid way or
* III (strategy #2) and is not compliant

<a name="15">[15]</a> The attacks in [[TPD](#TPD), [BBCPSTV](#BBCPSTV)] show that the security of GeMSS256, BlueGeMSS256 and RedGeMSS256 are less than level I

<a name="16">[16]</a> From [[RFC8554](#RFC8554)]

> If the public key is not exactly 24 + m bytes long, return INVALID

<a name="17">[17]</a> From [[RFC8391](#RFC8391)], see [Errata ID: 6024](https://www.rfc-editor.org/errata/eid6024)

> Parameters with SHA2 and n = 32 [...] and with SHA2 and n = 64 [...] yield post-quantum security of 128 and 256 bits, respectively. Parameters with SHAKE and n = 32 [...] [and] with SHAKE and n = 64 [...] yield post-quantum security of 86 and 170 bits, respectively.

and

> In consequence, SHAKE-128 cannot provide more security than NIST post-quantum security level II.

We then will consider in the table only the SHA-256 and SHAKE256 variants, other paramaters being not relevant in the context of [[ANSSI](#ANSSI)]

<a name="18">[18]</a> See Table 1 in [[KPCSA](#KPCSA)]

<a name="19">[19]</a> By assuming that `o1 = 36`, `o2 = 64` and `v1 = 148` which is coherent with the parameters in [[6](#6)], the formula in page 17 of the documentation gives the equation  `o1 * o2 + v1 * (o1 + o2) + o1 * o2 + o1 * (v1 * (v1 + 1) / 2 + v1 * o1) + o2 * ((v1 + o1) * (v1 + o1 + 1) / 2 + (v1 + o1) * o2)`

<a name="20">[20]</a> By modifying the code as proposed in [`script_test.sh`](script_test.sh), we obtain the following values

<a name="21">[21]</a> See Table 3 in [[KF](#KF)], for `2^20` messages for LMS and XMSS and `2^60` for HSS and XMSS-MT

<a name="22">[22]</a> See [[NIST2020](#NIST2020)]