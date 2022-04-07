# PQC tables

The goal of the following tables is to summarize the [ANSSI](#ANSSI) recommandations regarding post-quantum cryptography scheme usages for (French) certifications. These tables are subject to change depending on new cryptanalysis, new submitted algorithms to the [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography), new recommandations, etc. The simplified tables may give a quick overview of the ANSSI recommandations, while the larger tables will give more information, in particular about the sizes of the private key (sk), the public key (pk), the ciphertext (ct), the shared secret (ss) and the signature (sig).

## Tables (simplified)

### On the ANSSI column

According to [[ANSSI](#ANSSI)],

> Moreover the conjectured post-quantum level should be as high as possible, preferably NIST level V (AES-256).

> ANSSI encourages to use a conjectured post-quantum security level on symmetric primitives consistent with the selected post-quantum PKC algorithm – in practice at least the same security level as AES-256 for block ciphers and at least the same security level as SHA2-384 for hash functions.

We then consider, in the ANSSI column, that if a cryptographic scheme does not provide security parameters for level IV (at least as hard to break as SHA2-384) or level V (at least as hard to break as AES-256), the scheme is not suitable to be used to get a (French) certification.


### Post-quantum cryptography key exchange mechanisms and their usage for (French) certifications

| KEM                 | Variants (best security level) | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] |
| ---                 | ---                            | ---                  | ---                     |
| Classic McEliece    | 6960119(f), 8192128(f)         | Finalist             | Hybrid        [[7](#7)] |
| CRYSTALS-KYBER      | 1024                           | Finalist [[13](#13)] | Hybrid                  |
| NTRU                | HPS-4096-821                   | Finalist             | Maybe hybrid  [[1](#1)] |
| NTRU                | HPS-4096-1229, HRSS-1373       | Finalist             | Hybrid                  |
| SABER               | (u)FireSaber                   | Finalist             | Hybrid                  |
| BIKE                | Level 5                        | Alternate            | Hybrid                  |
| FrodoKEM            | 1344                           | Alternate            | Hybrid        [[8](#8)] |
| HQC                 | 256                            | Alternate            | Hybrid                  |
| NTRU Prime          | sntrup1277, ntrulpr1277        | Alternate            | Hybrid                  |
| SIKE                | p751                           | Alternate            | Hybrid                  |

### Post-quantum cryptography signatures and their usage for (French) certifications

| Signature           | Variants (best security level) | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] |
| ---                 | ---                            | ---                  | ---                     |
| Stateful hash-based | LMS, XMSS, HSS, XMSS-MT        | Standard [[10](#10)] | Compliant     [[9](#9)] |
| CRYSTALS-DILITHIUM  | 5                              | Finalist [[13](#13)] | Hybrid                  |
| FALCON              | 1024                           | Finalist [[13](#13)] | Hybrid                  |
| Rainbow             | V-Standard, V-CZ, V-compressed | Finalist             | Not compliant [[6](#6)] |
| GeMSS               | 256, all variants              | Alternate            | Hybrid                  |
| Picnic              | L5-FS, L5-UR, L5-full, 3-L5    | Alternate            | Hybrid                  |
| SPHINCS+            | 256s, 256f                     | Alternate            | Compliant     [[9](#9)] |

## Tables

### Notes

When two values in a cell, first is the one from the documentation, the second from the reference implementation submitted to [Round 3 submission of NIST Post-Quantum Cryptography](https://csrc.nist.gov/Projects/post-quantum-cryptography/round-3-submissions).

Other tables gathering data on PQC schemes can be found, for example at:

* [Algorithms in liboqs](https://openquantumsafe.org/liboqs/algorithms/);
* [PQC wiki](https://pqc-wiki.fau.edu/w/Special:DatabaseHome).

It is also possible to look for the different `api.h` or `META.yml` of [PQClean](https://github.com/PQClean/PQClean).

For performance benchmarks, an interested reader may refer to [eBACS](https://bench.cr.yp.to/ebats.html) or [pqm4](https://github.com/mupq/pqm4).

### Post-quantum cryptography key exchange mechanisms and their usage for (French) certification

| KEM                | Security Levels (claimed)    | Variant (best security levels) | Type                 | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] |  sk size (bytes)                  | pk size (bytes)                    | ct size (bytes)    | ss size (bytes)         |
| ---                | ---                          | ---                            | ---                  | ---                  | ---                     | ---                               | ---                                | ---                | ---                     |
| Classic McEliece   | I, III, V                    | 6960119(f)                     | Code                 | Finalist             | Hybrid        [[7](#7)] |                13,948             |              1,047,319             |    226             |          32             |
| Classic McEliece   | I, III, V                    | 8192128(f)                     | Code                 | Finalist             | Hybrid        [[7](#7)] |                14,120             |              1,357,824             |    240             |          32             |
| CRYSTALS-KYBER     | I, III, V                    | 1024                           | Lattice (structured) | Finalist             | Hybrid      [[13](#13)] |                 3,168             |                  1,568             |  1,568             |          32             |
| NTRU               | I, III, V [[3](#3)]          | HPS-4096-821                   | Lattice (structured) | Finalist             | Maybe hybrid  [[1](#1)] |                 1,590             |                  1,230             |  1.230             |          32             |
| NTRU               | I, III, V [[2](#2), [3](#3)] | HPS-4096-1229                  | Lattice (structured) | Finalist             | Hybrid                  |                 2,366   [[5](#5)] |                  1,842   [[5](#5)] |  1,842   [[5](#5)] |          32   [[5](#5)] |
| NTRU               | I, III, V [[2](#2), [4](#4)] | HRSS-1373                      | Lattice (structured) | Finalist             | Hybrid                  |                 2,938   [[5](#5)] |                  2,401   [[5](#5)] |  2.401   [[5](#5)] |          32   [[5](#5)] |
| SABER              | I, III, V                    | FireSaber                      | Lattice (structured) | Finalist             | Hybrid                  |                 3,040             |                  1,312             |  1.472             |          32             |
| SABER              | I, III, V                    | FireSaber, compressed          | Lattice (structured) | Finalist             | Hybrid                  |                 1,760 [[12](#12)] |                  1,312 [[12](#12)] |  1,472 [[12](#12)] |          32 [[12](#12)] |
| SABER              | I, III, V                    | uFireSaber                     | Lattice (structured) | Finalist             | Hybrid                  |                 2,912             |                  1,312             |  1.472             |          32             |
| SABER              | I, III, V                    | uFireSaber, compressed         | Lattice (structured) | Finalist             | Hybrid                  |                 1,632 [[12](#12)] |                  1,312 [[12](#12)] |  1,472 [[12](#12)] |          32 [[12](#12)] |
| BIKE               | I, III, V                    | Level 5                        | Code                 | Alternate            | Hybrid                  |                   580             |      5,122 /    10,276             |  5,154             |          32             |
| FrodoKEM           | I, III, V                    | 1344                           | Lattice              | Alternate            | Hybrid        [[8](#8)] |                43,088             |                 21,520             | 21,632             |          32             |
| HQC                | I, III, V                    | 256                            | Code                 | Alternate            | Hybrid                  |                  7285             |                  7,245             | 14,469             |          64             |
| NTRU Prime         | I, II, III, IV, V            | sntrup953          [[14](#14)] | Lattice (structured) | Alternate            | Hybrid                  |                 2,254             |                  1,505             |  1,349             |          32             |
| NTRU Prime         | I, II, III, IV, V            | ntrulpr953         [[14](#14)] | Lattice (structured) | Alternate            | Hybrid                  |                 1,652             |                  1,349             |  1,477             |          32             |
| NTRU Prime         | I, II, III, IV, V            | sntrup1013 (level IV)          | Lattice (structured) | Alternate            | Hybrid                  |                 2,417             |                  1,623             |  1,455             |          32             |
| NTRU Prime         | I, II, III, IV, V            | ntrulpr1013 (level IV)         | Lattice (structured) | Alternate            | Hybrid                  |                 1,773             |                  1,455             |  1,583             |          32             |
| NTRU Prime         | I, II, III, IV, V            | sntrup1277                     | Lattice (structured) | Alternate            | Hybrid                  |                 3,059             |                  2,067             |  1,847             |          32             |
| NTRU Prime         | I, II, III, IV, V            | ntrulpr1277                    | Lattice (structured) | Alternate            | Hybrid                  |                 2,231             |                  1,847             |  1,975             |          32             |
| SIKE               | I, II, III, V                | p751                           | Isogenies            | Alternate            | Hybrid                  |                   644             |                    564             |    596             |          32             |
| SIKE               | I, II, III, V                | p751, compressed               | Isogenies            | Alternate            | Hybrid                  |                   602             |                    335             |    410             |          32             |

### Post-quantum cryptography signatures and their usage for (French) certification

| Signature          | Security Levels (claimed)    | Variant (best security levels) | Type                 | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] | sk size (bytes)                 |  pk size (bytes)                   | sig size (bytes)  |
| ---                | ---                          | ---                            | ---                  | ---                  | ---                     | ---                             |  ---                               | ---               |
| LMS                | V                            | 256-bit hash                   | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |             Dependent           |                     56 [[11](#11)] |         Dependent |
| HSS                | V                            | 256-bit hash                   | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |             Dependent           |                     60 [[11](#11)] |         Dependent |
| XMSS               | V                            | 256-bit hash                   | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |             Dependent           |                     68 [[11](#11)] |         Dependent |
| XMSS-MT            | V                            | 256-bit hash                   | Hash (stateful)      | Standard [[10](#10)] | Compliant     [[9](#9)] |             Dependent           |                     68 [[11](#11)] |         Dependent |
| CRYSTALS-DILITHIUM | II, III, V                   | 5                              | Lattice (structured) | Finalist             | Hybrid      [[13](#13)] |                 4,880 [[5](#5)] |                  2,592             |             4,595 |
| FALCON             | I, V                         | 1024                           | Lattice (structured) | Finalist             | Hybrid      [[13](#13)] |                 2,305 [[5](#5)] |                  1,793             |   1,280 /   1,330 |
| Rainbow            | I, III [[6](#6)]             | V-Standard                     | Multivariate         | Finalist             | Not compliant           | 1,375,700 / 1,408,736           |  1,885,400 / 1,930,600             |               212 |
| Rainbow            | I, III [[6](#6)]             | V-CZ                           | Multivariate         | Finalist             | Not compliant           | 1,375,700 / 1,408,736           |    523,600 /   536,136             |               212 |
| Rainbow            | I, III [[6](#6)]             | V-Compressed                   | Multivariate         | Finalist             | Not compliant           |                    64           |    523,600 /   536,136             |               212 |
| GeMSS              | I, III, V                    | GeMSS256                       | Multivariate         | Alternate            | Hybrid                  |                    32           |              3,040,700             |                72 |
| GeMSS              | I, III, V                    | BlueGeMSS256                   | Multivariate         | Alternate            | Hybrid                  |                    32           |              3,087,963             |                74 |
| GeMSS              | I, III, V                    | CyanGeMSS256                   | Multivariate         | Alternate            | Hybrid                  |                    32           |              3,272,017             |                66 |
| GeMSS              | I, III, V                    | RedGeMSS256                    | Multivariate         | Alternate            | Hybrid                  |                    32           |              3,135,591             |                75 |
| GeMSS              | I, III, V                    | MagentaGeMSS256                | Multivariate         | Alternate            | Hybrid                  |                    32           |              3,321,717             |                67 |
| GeMSS              | I, III, V                    | WhiteGeMSS256                  | Multivariate         | Alternate            | Hybrid                  |                    32           |              3,222,691             |                65 |
| Picnic             | I, III, V                    | L5-FS                          | ZKP / Symmetric      | Alternate            | Hybrid                  |        32 /        97           |         64 /        65             | 132,856 / 132,876 |
| Picnic             | I, III, V                    | L5-UR                          | ZKP / Symmetric      | Alternate            | Hybrid                  |        32 /        97           |         64 /        65             | 209,506 / 209,526 |
| Picnic             | I, III, V                    | L5-full                        | ZKP / Symmetric      | Alternate            | Hybrid                  |        32 /        97           |         64 /        65             |           126,286 |
| Picnic             | I, III, V                    | 3-L5                           | ZKP / Symmetric      | Alternate            | Hybrid                  |        32 /        97           |         64 /        65             |  54,732 /  61,028 |
| SPHINCS+           | I, III, V                    | 256s                           | Hash (stateless)     | Alternate            | Compliant     [[9](#9)] |                   128           |                     64             |            29,792 |
| SPHINCS+           | I, III, V                    | 256f                           | Hash (stateless)     | Alternate            | Compliant     [[9](#9)] |                   128           |                     64             |            49,856 |

## Explanations

<a name="ANSSI">[ANSSI]</a> [ANSSI views on the Post-Quantum Cryptography transition](https://www.ssi.gouv.fr/publication/anssi-views-on-the-post-quantum-cryptography-transition/)

<a name="BSI">[BSI]</a> [Migration zu Post-Quanten-Kryptografie](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Krypto/Post-Quanten-Kryptografie.html) and [BSI TR-02102-1: "Cryptographic Mechanisms: Recommendations and Key Lengths" Version: 2022-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.html)

<a name="NIST">[NIST]</a> [Status Report on the Second Round of the NIST Post-Quantum Cryptography Standardization Process](https://csrc.nist.gov/publications/detail/nistir/8309/final)

<a name="1">[1]</a> Not compliant if conservative choice (non-local) for the computational model, Hybrid otherwise

<a name="2">[2]</a> [Category 5 NTRU parameters](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/t1JCgzSS-uk/m/H9M8jdQDCQAJ)

<a name="3">[3]</a> I & III (non-local), I, III, V (local), not taking into account the parameters in [[2](#2)]

<a name="4">[4]</a> I (non-local), III (local), not taking into account the parameters in [[2](#2)]

<a name="5">[5]</a> Only from the code

<a name="6">[6]</a> [ROUND 3 OFFICIAL COMMENT: Rainbow](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/KFgw5_qCXiI/m/cr66AGOfAgAJ)

<a name="7">[7]</a> From [[BSI](#BSI)]

> The mechanisms FrodoKEM-976, FrodoKEM-1344 as well as **Classic McEliece** with the parameters in **Categories 3 and 5** are assessed to be cryptographically suitable to protect confidential.

<a name="8">[8]</a> From [[ANSSI](#ANSSI)] and [[BSI](#BSI)]

> For example, a developer should be able to obtain a security visa for a product implementing FrodoKEM whether NIST decides that FrodoKEM will be one of the first PQC standards or not.

> The mechanisms FrodoKEM-976, **FrodoKEM-1344** as well as Classic McEliece with the parameters in Categories 3 and 5 are assessed to be cryptographically suitable to protect confidential.

<a name="9">[9]</a> From [[ANSSI](#ANSSI)]

> Hash-based signatures are an exception for hybridation: due to their well-studied underlying mathematical problem, ANSSI estimates that these algorithms could be used today without hybridation. However, their potential application range is limited (low number of signatures queries or large signature sizes).

<a name="10">[10]</a> [Recommendation for Stateful Hash-Based Signature Schemes](https://doi.org/10.6028/NIST.SP.800-208)

<a name="11">[11]</a> [LMS vs XMSS: Comparison of Stateful Hash-Based Signature Schemes on ARM Cortex-M4](https://eprint.iacr.org/2020/470), Table 2

<a name="12">[12]</a> Only from the documentation

<a name="13">[13]</a> From[[ANSSI](#ANSSI)]

> For example, at the time of the writing, the NIST candidates FrodoKEM, **Kyber, Dilithium or Falcon** could be good options for first deployments.

<a name="14">[14]</a> Depending on the analysis of the security level (bulletproofing strategies), the security level is IV (strategy #1) or III (strategy #2)
