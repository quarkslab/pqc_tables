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

### Notes

We give in notes some additional content, either to justify our results or to give more information and some recommendations, coming from the ANSSI views or from other governments’ positions. Indeed, as mentioned in [ANSSI](#ANSSI),

> Several governments have published similar position papers recommending to prepare the post-quantum transition. ANSSI’s views are similar to the BSI’s position on many issues (e.g. necessary migration, hybridation, cryptoagility).

Even if these tables are focused on the French context, they may be used in other national contexts too.

### Post-quantum cryptography key exchange mechanisms and their usage for (French) certifications

| KEM                 | Variants (best security level)               | NIST [[NIST](#NIST)] | ANSSI   [[ANSSI](#ANSSI)] |
| ---                 | ---                                          | ---                  | ---                       |
| Classic McEliece    | 6960119(f), 8192128(f)                       | Finalist             | Hybrid          [[7](#7)] |
| CRYSTALS-KYBER      | 1024                                         | Finalist [[13](#13)] | Hybrid                    |
| NTRU                | HPS-4096-821                                 | Finalist             | Maybe hybrid    [[1](#1)] |
| NTRU                | HPS-4096-1229, HRSS-1373                     | Finalist             | Hybrid                    |
| SABER               | (u)FireSaber                                 | Finalist             | Hybrid                    |
| BIKE                | Level 5                                      | Alternate            | Hybrid                    |
| FrodoKEM            | 1344                                         | Alternate            | Hybrid          [[8](#8)] |
| HQC                 | 256                                          | Alternate            | Hybrid                    |
| NTRU Prime          | sntrup1277, ntrulpr1277                      | Alternate            | Hybrid                    |
| SIKE                | p751                                         | Alternate            | Hybrid                    |

### Post-quantum cryptography signatures and their usage for (French) certifications

| Signature           | Variants (best security level)               | NIST [[NIST](#NIST)] | ANSSI   [[ANSSI](#ANSSI)] |
| ---                 | ---                                          | ---                  | ---                       |
| Stateful hash-based | LMS, XMSS, HSS, XMSS-MT                      | Standard [[10](#10)] | Compliant       [[9](#9)] |
| CRYSTALS-DILITHIUM  | 5                                            | Finalist [[13](#13)] | Hybrid                    |
| FALCON              | 1024                                         | Finalist [[13](#13)] | Hybrid                    |
| Rainbow             | UOV parameters SL5   [[6](#6)]               | Finalist             | Compliant                 |
| GeMSS               | 256, all variants                            | Alternate            | Not compliant [[15](#15)] |
| Picnic              | L5-FS, L5-UR, L5-full, 3-L5                  | Alternate            | Hybrid                    |
| SPHINCS+            | SHAKE-256s, SHA2-256s, SHAKE-256f, SHA2-256s | Alternate            | Compliant       [[9](#9)] |

## Tables

### Notes

When two values are in a same cell, first is the one from the documentation, the second from the reference implementation submitted to [Round 3 submission of NIST Post-Quantum Cryptography](https://csrc.nist.gov/Projects/post-quantum-cryptography/round-3-submissions).

Other tables gathering data on PQC schemes can be found, for example at:

* [Algorithms in liboqs](https://openquantumsafe.org/liboqs/algorithms/);
* [[ETSIKEM](#ETSIKEM)] and [[ETSISIG](#ETSISIG)];
* [PQC wiki](https://pqc-wiki.fau.edu/w/Special:DatabaseHome);

It is also possible to look for the different `api.h` or `META.yml` of [PQClean](https://github.com/PQClean/PQClean).

For performance benchmarks, an interested reader may refer to [eBACS](https://bench.cr.yp.to/ebats.html) or [pqm4](https://github.com/mupq/pqm4).

In the variants of LMS, HSS, XMSS and XMSS-MT, the `..` or `../..` refers to the paramaters given:

* for LMS, in Table 2 of [[RFC8554](#RFC8554)];
* for XMSS, in Table 2 of [[RFC8391](#RFC8391)];
* for XMSS-MT, in Table 4 of [[RFC8391](#RFC8391)].

### Post-quantum cryptography key exchange mechanisms and their usage for (French) certification

| KEM                | Security Levels        | Variant (best security levels)          | Type                 | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] |  sk size (bytes)   | pk size (bytes)               | ct size (bytes)    | ss size (bytes) |
| ---                | ---                    | ---                                     | ---                  | ---                  | ---                     | ---                | ---                           | ---                | ---             |
| Classic McEliece   | I, III, V              | 6960119(f)                              | Code                 | Finalist             | Hybrid        [[7](#7)] | 13,948             |         1,047,319             |    226             | 32              |
| Classic McEliece   | I, III, V              | 8192128(f)                              | Code                 | Finalist             | Hybrid        [[7](#7)] | 14,120             |         1,357,824             |    240             | 32              |
| CRYSTALS-KYBER     | I, III, V              | 1024                                    | Lattice (structured) | Finalist             | Hybrid      [[13](#13)] |  3,168             |             1,568             |  1,568             | 32              |
| NTRU               | I, III, V              | HPS-4096-821 (level III / V)  [[3](#3)] | Lattice (structured) | Finalist             | Maybe hybrid  [[1](#1)] |  1,590             |             1,230             |  1.230             | 32              |
| NTRU               | I, III, V              | HPS-4096-1229        [[2](#2), [3](#3)] | Lattice (structured) | Finalist             | Hybrid                  |  2,366   [[5](#5)] |             1,842   [[5](#5)] |  1,842   [[5](#5)] | 32    [[5](#5)] |
| NTRU               | I, III, V              | HRSS-1373            [[2](#2), [4](#4)] | Lattice (structured) | Finalist             | Hybrid                  |  2,938   [[5](#5)] |             2,401   [[5](#5)] |  2.401   [[5](#5)] | 32    [[5](#5)] |
| SABER              | I, III, V              | FireSaber                               | Lattice (structured) | Finalist             | Hybrid                  |  3,040             |             1,312             |  1.472             | 32              |
| SABER              | I, III, V              | FireSaber, compressed                   | Lattice (structured) | Finalist             | Hybrid                  |  1,760 [[12](#12)] |             1,312 [[12](#12)] |  1,472 [[12](#12)] | 32  [[12](#12)] |
| SABER              | I, III, V              | uFireSaber                              | Lattice (structured) | Finalist             | Hybrid                  |  2,912             |             1,312             |  1.472             | 32              |
| SABER              | I, III, V              | uFireSaber, compressed                  | Lattice (structured) | Finalist             | Hybrid                  |  1,632 [[12](#12)] |             1,312 [[12](#12)] |  1,472 [[12](#12)] | 32  [[12](#12)] |
| BIKE               | I, III, V              | Level 5                                 | Code                 | Alternate            | Hybrid                  |    580             | 5,122 /    10,276             |  5,154             | 32              |
| FrodoKEM           | I, III, V              | 1344                                    | Lattice              | Alternate            | Hybrid        [[8](#8)] | 43,088             |            21,520             | 21,632             | 32              |
| HQC                | I, III, V              | 256                                     | Code                 | Alternate            | Hybrid                  |  7,285             |             7,245             | 14,469             | 64              |
| NTRU Prime         | I, II, III, IV, V      | sntrup953 (level III / IV)  [[14](#14)] | Lattice (structured) | Alternate            | Maybe hybrid            |  2,254             |             1,505             |  1,349             | 32              |
| NTRU Prime         | I, II, III, IV, V      | ntrulpr953 (level III / IV) [[14](#14)] | Lattice (structured) | Alternate            | Maybe hybrid            |  1,652             |             1,349             |  1,477             | 32              |
| NTRU Prime         | I, II, III, IV, V      | sntrup1013 (level IV)                   | Lattice (structured) | Alternate            | Hybrid                  |  2,417             |             1,623             |  1,455             | 32              |
| NTRU Prime         | I, II, III, IV, V      | ntrulpr1013 (level IV)                  | Lattice (structured) | Alternate            | Hybrid                  |  1,773             |             1,455             |  1,583             | 32              |
| NTRU Prime         | I, II, III, IV, V      | sntrup1277                              | Lattice (structured) | Alternate            | Hybrid                  |  3,059             |             2,067             |  1,847             | 32              |
| NTRU Prime         | I, II, III, IV, V      | ntrulpr1277                             | Lattice (structured) | Alternate            | Hybrid                  |  2,231             |             1,847             |  1,975             | 32              |
| SIKE               | I, II, III, V          | p751                                    | Isogenies            | Alternate            | Hybrid                  |    644             |               564             |    596             | 32              |
| SIKE               | I, II, III, V          | p751, compressed                        | Isogenies            | Alternate            | Hybrid                  |    602             |               335             |    410             | 32              |

### Post-quantum cryptography signatures and their usage for (French) certification

| Signature          | Security Levels        | Variants (best security levels)         | Type                 | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] | sk size (bytes)                               |  pk size (bytes)                                        | sig size (bytes)              |
| ---                | ---                    | ---                                     | ---                  | ---                  | ---                     | ---                                           |  ---                                                    | ---                           |
| LMS                | V          [[18](#18)] | `LMS_SHA256_M32_H..`                    | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |                         Dependent             |                                          56 [[16](#16)] |         Dependent             |
| HSS                | V          [[18](#18)] | with `LMS_SHA256_M32_H..`               | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |                         Dependent             |                                          60 [[11](#11)] |         Dependent             |
| XMSS               | II, V      [[17](#17)] | `XMSS-SHA2_.._256`                      | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |                         Dependent             |                                          68 [[11](#11)] |         Dependent             |
| XMSS               | II, V      [[17](#17)] | `XMSS-SHAKE_.._512`                     | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |                         Dependent             |                                         132 [[11](#11)] |         Dependent             |
| XMSS-MT            | II, V      [[17](#17)] | `XMSSMT-SHA2_../.._256`                 | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |                         Dependent             |                                          68 [[11](#11)] |         Dependent             |
| XMSS-MT            | II, V      [[17](#17)] | `XMSSMT-SHAKE_../.._512`                | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |                         Dependent             |                                         132 [[11](#11)] |         Dependent             |
| CRYSTALS-DILITHIUM | II, III, V             | 5                                       | Lattice (structured) | Finalist             | Hybrid      [[13](#13)] |                             4,880   [[5](#5)] |                                       2,592             |             4,595             |
| FALCON             | I, V                   | 1024                                    | Lattice (structured) | Finalist             | Hybrid      [[13](#13)] |                             2,305   [[5](#5)] |                                       1,793             |   1,280 /   1,330             |
| Rainbow            | I, III, V    [[6](#6)] | UOV parameters SL5-Standard             | Multivariate         | Finalist             | Compliant               | 2,451,096 [[19](#19)] / 2,451,128 [[20](#20)] | 2,869,440 [[6](#6), [[12](#12)] / 3,087,600 [[20](#20)] |               264 [[20](#20)] |
| Rainbow            | I, III, V    [[6](#6)] | UOV parameters SL5-CZ                   | Multivariate         | Finalist             | Compliant               | 2,451,096 [[19](#19)] / 2,451,128 [[20](#20)] |                                     655,944 [[20](#20)] |               264 [[20](#20)] |
| GeMSS              | < I        [[15](#15)] | GeMSS256                                | Multivariate         | Alternate            | Not compliant           |                                32             |                                   3,040,700             |                72             |
| GeMSS              | < I        [[15](#15)] | BlueGeMSS256                            | Multivariate         | Alternate            | Not compliant           |                                32             |                                   3,087,963             |                74             |
| GeMSS              | < I        [[15](#15)] | CyanGeMSS256                            | Multivariate         | Alternate            | Not compliant           |                                32             |                                   3,272,017             |                66             |
| GeMSS              | < I        [[15](#15)] | RedGeMSS256                             | Multivariate         | Alternate            | Not compliant           |                                32             |                                   3,135,591             |                75             |
| GeMSS              | < I        [[15](#15)] | MagentaGeMSS256                         | Multivariate         | Alternate            | Not compliant           |                                32             |                                   3,321,717             |                67             |
| GeMSS              | < I        [[15](#15)] | WhiteGeMSS256                           | Multivariate         | Alternate            | Not compliant           |                                32             |                                   3,222,691             |                65             |
| Picnic             | I, III, V              | L5-FS                                   | ZKP / Symmetric      | Alternate            | Hybrid                  |        32             /        97             |           64                    /        65             | 132,856 / 132,876             |
| Picnic             | I, III, V              | L5-UR                                   | ZKP / Symmetric      | Alternate            | Hybrid                  |        32             /        97             |           64                    /        65             | 209,506 / 209,526             |
| Picnic             | I, III, V              | L5-full                                 | ZKP / Symmetric      | Alternate            | Hybrid                  |        32             /        97             |           64                    /        65             |           126,286             |
| Picnic             | I, III, V              | 3-L5                                    | ZKP / Symmetric      | Alternate            | Hybrid                  |        32             /        97             |           64                    /        65             |  54,732 /  61,028             |
| SPHINCS+           | I, II, III, V          | SHAKE-256s, SHA2-256s                   | Hash (stateless)     | Alternate            | Compliant     [[9](#9)] |                               128             |                                          64             |            29,792             |
| SPHINCS+           | I, II, III, V          | SHAKE-256f, SHA2-256f                   | Hash (stateless)     | Alternate            | Compliant     [[9](#9)] |                               128             |                                          64             |            49,856             |

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

<a name="NIST">[NIST]</a> G. Alagic, J. Alperin-Sheriff, D. Apon, D. Cooper, Q. Dang, J. Kelsey, Y.-K. Liu, C. Miller, D. Moody, R. Peralta, R. Perlner, A. Robinson and D. Smith-Tone, [Status Report on the Second Round of the NIST Post-Quantum Cryptography Standardization Process](https://csrc.nist.gov/publications/detail/nistir/8309/final), NISTIR 8309, July 2020

<a name="NISTSTD">[NISTSTD]</a> D. Cooper, D. Apon, Q. Dang, M. Davidson, M. Dworkin, and C. Miller, [Recommendation for Stateful Hash-Based Signature Schemes](https://doi.org/10.6028/NIST.SP.800-208), NIST Special Publication 800-208, October 2020

<a name="NLNCSA">[NLNCSA]</a> [Prepare for the threat of quantum-computers](https://english.aivd.nl/publications/publications/2022/01/18/prepare-for-the-threat-of-quantumcomputers), 18 January 2022 

<a name="RFC8391">[RFC8391]</a> A. Huelsing, D. Butin, S. Gazdag, J. Rijneveld and A. Mohaisen, [XMSS: eXtended Merkle Signature Scheme](https://datatracker.ietf.org/doc/html/rfc8391), RFC 8391, May 2018

<a name="RFC8554">[RFC8554]</a> D. McGrew, M. Curcio and S. Fluhrer, [Leighton-Micali Hash-Based Signatures](https://datatracker.ietf.org/doc/html/rfc8554), RFC8554, April 2019

<a name="SFG">[SFG]</a> D. Stebila, S. Fluhrer and S. Gueron, [Hybrid key exchange in TLS 1.3](https://datatracker.ietf.org/doc/html/draft-ietf-tls-hybrid-design-04), Network Working Group, Internet-Draft, 11 January 2022

<a name="TPD">[TPD]</a> C. Tao, A. Petzoldt and J. Ding, [Efficient Key Recovery for All HFE Signature Variants](https://doi.org/10.1007/978-3-030-84242-0_4). In: T. Malkin and C. Peikert (eds), CRYPTO 2021. LNCS, vol. 12825, pp. 70-93. Springer (11 August 2021)

<a name="1">[1]</a> Not compliant if conservative choice (non-local) for the computational model, Hybrid otherwise

<a name="2">[2]</a> [Category 5 NTRU parameters](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/t1JCgzSS-uk/m/H9M8jdQDCQAJ)

<a name="3">[3]</a> I & III (non-local), I & III & V (local), not taking into account the parameters in [[2](#2)]

<a name="4">[4]</a> I (non-local), III (local), not taking into account the parameters in [[2](#2)]

<a name="5">[5]</a> Only from the code

<a name="6">[6]</a> After the attack in [[Beu](#Beu)] acknowledged in [ROUND 3 OFFICIAL COMMENT: Rainbow](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/KFgw5_qCXiI/m/cr66AGOfAgAJ), the authors proposed a new set of parameters [UOV parameters](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/B1RFy31rH8I/m/yIqAt7dABAAJ)

<a name="7">[7]</a> From [[BSI](#BSI)] and [[NLNCSA](#NLNCSA)]

> The mechanisms FrodoKEM-976, FrodoKEM-1344 as well as **Classic McEliece** with the parameters in **Categories 3 and 5** are assessed to be cryptographically suitable to protect confidential.

> For PQC, we recommend the most secure algorithms, such as Frodo or **McEliece**.

<a name="8">[8]</a> From [[ANSSI](#ANSSI)], [[BSI](#BSI)] and [[NLNCSA](#NLNCSA)]

> For example, a developer should be able to obtain a security visa for a product implementing FrodoKEM whether NIST decides that FrodoKEM will be one of the first PQC standards or not.

> The mechanisms FrodoKEM-976, **FrodoKEM-1344** as well as Classic McEliece with the parameters in Categories 3 and 5 are assessed to be cryptographically suitable to protect confidential.

> For PQC, we recommend the most secure algorithms, such as **Frodo** or McEliece.

<a name="9">[9]</a> From [[ANSSI](#ANSSI)]

> Hash-based signatures are an exception for hybridation: due to their well-studied underlying mathematical problem, ANSSI estimates that these algorithms could be used today without hybridation. However, their potential application range is limited (low number of signatures queries or large signature sizes).

<a name="10">[10]</a> See [[NISTSTD](#NISTSTD)], [[RFC8391](#RFC8391)] and [[RFC8554](#RFC8554)]

<a name="11">[11]</a> See Table 2 in [[KF](#KF)]

<a name="12">[12]</a> Only from the documentation

<a name="13">[13]</a> From [[ANSSI](#ANSSI)]

> For example, at the time of the writing, the NIST candidates FrodoKEM, **Kyber, Dilithium or Falcon** could be good options for first deployments.

<a name="14">[14]</a> Depending on the analysis of the security level (bulletproofing strategies), the security level is IV (strategy #1) or III (strategy #2)

<a name="15">[15]</a> The attacks in [[TPD](#TPD), [BBCPSTV](#BBCPSTV)] show that the security of GeMSS256, BlueGeMSS256 and RedGeMSS256 are less than level I

<a name="16">[16]</a> From [[RFC8554](#RFC8554)]

> If the public key is not exactly 24 + m bytes long, return INVALID

<a name="17">[17]</a> From [[RFC8391](#RFC8391)], see [Errata ID: 6024](https://www.rfc-editor.org/errata/eid6024)

> Parameters with SHA2 and n = 32 [...] and with SHA2 and n = 64 [...] yield post-quantum security of 128 and 256 bits, respectively. Parameters with SHAKE and n = 32 [...] [and] with SHAKE and n = 64 [...] yield post-quantum security of 86 and 170 bits, respectively.

> In consequence, SHAKE-128 cannot provide more security than NIST post-quantum security level II.

We then will consider in the table only the SHA-256 and SHAKE256 variants, other paramaters being not relevant in the context of [[ANSSI](#ANSSI)]

<a name="18">[18]</a> See Table 1 in [[KPCSA](#KPCSA)]

<a name="19">[19]</a> By assuming that `o1 = 36`, `o2 = 64` and `v1 = 148` which is coherent with the parameters in [[6](#6)], the formula in page 17 of the documentation gives the equation  `o1 * o2 + v1 * (o1 + o2) + o1 * o2 + o1 * (v1 * (v1 + 1) / 2 + v1 * o1) + o2 * ((v1 + o1) * (v1 + o1 + 1) / 2 + (v1 + o1) * o2)`

<a name="20">[20]</a> By modifying the code as proposed in [`script_test.sh`](script_test.sh), we obtain the following values
