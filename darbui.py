# importing modules from packages
from sqlalchemy import *
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import *
from tkinter import Toplevel

engine = create_engine('sqlite:///language.db', echo=True)
Base = declarative_base()
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

class Languages_all(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    lang = Column('language', String, unique=True, nullable=False)
    text = Column('company_rules', String, nullable=False)
    agree = Column('Agree button', String, default='None', nullable=True)


    def __init__(self, lang, text, agree):
        self.lang = lang
        self.text = text
        self.agree = agree

    def __repr__(self):
        return f"{self.id}, {self.lang}, {self.text}, {self.agree}"


Base.metadata.create_all(engine)
# tekstas = Users(lang='lietuvių', text = """
# Į UŽSIENIEČIŲ REGISTRACIJOS CENTRĄ ATVYKUSIEMS AR PRISTATYTIEMS BEI APGYVENDINTIEMS UŽSIENIEČIAMS
#
#   I. BENDROSIOS NUOSTATOS
#
# 	1. Informacinis lapas į Užsieniečių registracijos centrą (toliau - centras) atvykusiems ar pristatytiems bei apgyvendintiems užsieniečiams yra paruoštas vadovaujantis Lietuvos Respublikos įstatymu „Dėl užsieniečių teisinės padėties“, Laikinojo užsieniečių apgyvendinimo centre sąlygų ir tvarkos aprašu bei Laikinai centre apgyvendintų užsieniečių vidaus tvarkos taisyklėmis.
#
# 	2. Centro adresas ir kontaktai:
# 	Valstybės sienos apsaugos tarnybos prie
# 	Lietuvos Respublikos vidaus reikalų ministerijos
# 	Užsieniečių registracijos centras
# 	Vilniaus gatvė 100
# 	LT-18177
# 	Pabradės miestas
# 	Švenčionių rajonas
# 	Lietuvos Respublika
# 	Faksas -  +370 387 63012
# 	e. paštas – urc.sekretore@vsat.vrm.lt
#
# II. CENTRE APGYVENDINAMI ASMENYS
#
# 	3. Centre apgyvendinami šie asmenys:
# 	3.1. neteisėtai atvykę į Lietuvos Respubliką ar neteisėtai esantys Lietuvos Respublikoje užsieniečiai (toliau - sulaikyti užsieniečiai) – teismo sprendimu;
# 	3.2. sulaikyti užsieniečiai, pateikę prašymus suteikti prieglobstį Lietuvos Respublikoje (toliau - sulaikyti prieglobsčio prašytojai) – teismo sprendimu;
# 	3.3. užsieniečiai, atvykę patys ir pateikę centrui prašymus suteikti prieglobstį Lietuvos Respublikoje, iki bus priimtas Migracijos departamento prie Vidaus reikalų ministerijos (toliau- Migracijos departamentas) sprendimas suteikti arba nesuteikti jiems laikiną teritorinį prieglobstį Lietuvos Respublikoje – centro viršininko sprendimu;
# 	3.4. užsieniečiai, pateikę prašymus suteikti prieglobstį kitoms Lietuvos Respublikos teisėsaugos įstaigoms ir institucijoms (toliau ¬- prieglobsčio prašytojai) – Migracijos departamento ar teismo sprendimu;
# 3.5. prieglobsčio prašytojai, apgyvendinti alternatyvia sulaikymui priemone, nustatant teisę judėti tik centro teritorijoje;
# 	3.6. teisėtai į Lietuvos Respubliką atvykę prieglobsčio prašytojai, kuriems suteiktas laikinas teritorinis prieglobstis – Migracijos departamento sprendimu;
# 	4. Centre neapgyvendinami nelydimi nepilnamečiai užsieniečiai.
#
# III. APGYVENDINIMAS CENTRE
#
# 	5. Sulaikyti užsieniečiai apgyvendinami atskirai nuo sulaikytų prieglobsčio prašytojų.
# 	6. Prieglobsčio prašytojai apgyvendinami atskirai nuo sulaikytų užsieniečių ir sulaikytų prieglobsčio prašytojų.
# 	7. Vyrai apgyvendinami atskirai nuo moterų.
# 	8.Užtikrinant atitinkamą privatumą vienos šeimos nariai apgyvendinami kartu atskiroje gyvenamojoje patalpoje arba greta esančiose, viena nuo kitos neizoliuotose gyvenamosiose patalpose, išskyrus atvejus, kai vienas iš šeimos narių prieštarauja tokiam apgyvendinimui ir tam yra objektyvios priežastys.
# 	9. Asmenys gali būti apgyvendinami suskirstant į grupes (pagal kilmės valstybę, išpažįstamą religiją, pavojingumą savo ir aplinkinių sveikatai ir kitais pagrindais).
# 10. Priimdamas naujai atvykusį ar pristatytą užsienietį, centro Apsaugos skyriaus pareigūnas atlieka užsieniečio apžiūrą ir daiktų patikrinimą bei surašo asmens apžiūros ir daiktų patikrinimo protokolą. Užsieniečio apžiūrą atlieka tos pačios lyties asmuo, kaip apžiūrimasis. Išskirtiniais atvejais, jei pareigūnas tikrina kitos lyties asmenį, būtina, kad dalyvautų kviestiniai asmenys. Užsieniečio daiktai tikrinami dalyvaujant daiktų savininkui. Tais atvejais, kai daiktų tikrinimo atidėti negalima, jie gali būti patikrinti ir be savininko, dalyvaujant dviem kviestiniams asmenims.
# 11. Po apžiūros daiktai, kuriuos centre turėti leidžiama, užsieniečiui grąžinami. Jų saugumu rūpinasi pats asmuo. Daiktai, kuriuos užsieniečiams centre turėti draudžiama, paimami ir saugomi nustatyta tvarka. Užsieniečiui yra išduodama asmens apžiūros ir daiktų patikrinimo protokolo kopija.
# 	12. Naujai atvykęs ar pristatytas užsienietis pasirašytinai supažindinamas su centro vidaus tvarkos taisyklėmis. Užpildo apgyvendinamo užsieniečio apklausos anketą.
# 	13. Naujai į centrą pristatyti sulaikyti užsieniečiai apgyvendinami karantino patalpose. Į bendras gyvenamąsias patalpas užsieniečiai perkeliami po medicininės apžiūros, įsitikinus, kad jie neserga pavojingomis ar ypač pavojingomis užkrečiamosiomis ligomis. Medicininę apžiūrą atlieka centre dirbantis medicinos personalas.
#
# 	IV. APGYVENDINIMO CENTRE TRUKMĖ
#
# 	14. Užsienietis negali būti sulaikomas ilgiau kaip 6 mėnesiams, išskyrus atvejus, kai jis nebendradarbiauja siekiant jį išsiųsti iš Lietuvos Respublikos (atsisako pateikti apie save duomenis, teikia klaidinančią informaciją ir pan.) arba negaunami reikiami dokumentai tokio užsieniečio išsiuntimui iš valstybės teritorijos įvykdyti. Šiais atvejais sulaikymo terminas gali būti pratęstas papildomam, ne ilgesniam kaip 12 mėnesių, laikotarpiui.
#
# """ , agree='Perskaičiau ir sutinku')
# session.add(tekstas)

#
# session.commit()
# session.close()