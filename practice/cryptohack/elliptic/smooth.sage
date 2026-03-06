# taken from https://github.com/elikaski/ECC_Attacks?tab=readme-ov-file#The-order-of-the-generator-is-a-smooth-number

p = 310717010502520989590157367261876774703
a = 2
b = 3
E = EllipticCurve(GF(p), [a,b])
g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = E(g_x, g_y)
n = G.order()
print("number of bits in n:", n.nbits())
print("n's factors:", n.factor())
print("number of bits in n's greatest factor:", n.factor()[-1][0].nbits())

#Point(x=280810182131414898730378982766101210916, y=291506490768054478159835604632710368904)
pub_x = 280810182131414898730378982766101210916
pub_y = 291506490768054478159835604632710368904
A = E(pub_x, pub_y)
print("Calculating discrete_log...")
found_key = G.discrete_log(A)
assert found_key * G == A
print("success!")

print(found_key)

p = 310717010502520989590157367261876774703
a = 2
b = 3
E = EllipticCurve(GF(p), [a,b])
found_key = 47836431801801373761601790722388100620

n_A = 47836431801801373761601790722388100620
b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = E(b_x, b_y)
key = found_key * B

print(key)

# (171172176587165701252669133307091694084 : 188106434727500221954651940996276684440 : 1)