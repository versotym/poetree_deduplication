

def adhoc_cases(lang):
    '''
    This function enumerates components that needs to be treated individually 
    (can not be solved by rules in rules.py).
    For each language it returns a dict where key is a poem's id and
    value is either False (for the one we keep) or id of the poem
    current one is considered to be a duplicate of.
    '''

    # ------------ CS ---------------------------------------------------------
    
    if lang == 'cs':
        
        return {
            # Poem is published twice as a whole (P1, P6) and then once splitted into parts.
            # Wholes are connected and then each part is connected to both of them
            # => Keep the oldest + longest version (P1)            
            '0742_0-0000-0000-0016-0000'    : False,                           # (P1) Neruda, Jan : O Šimonu Lomnickém. n=317
            '0692_0002-0001-0000-0003-0001' : '0742_0-0000-0000-0016-0000',    # (P2) Neruda, Jan : O ŠIMONU LOMNICKÉM (1) n=28
            '0692_0002-0001-0000-0003-0005' : '0742_0-0000-0000-0016-0000',    # (P3) Neruda, Jan : O ŠIMONU LOMNICKÉM (5) n=36
            '0692_0002-0001-0000-0003-0006' : '0742_0-0000-0000-0016-0000',    # (P4) Neruda, Jan : O ŠIMONU LOMNICKÉM (6) n=113
            '0692_0002-0001-0000-0003-0002' : '0742_0-0000-0000-0016-0000',    # (P5) Neruda, Jan : O ŠIMONU LOMNICKÉM (2) n=42
            '0696_0001-0000-0000-0003-0000' : '0742_0-0000-0000-0016-0000',    # (P6) Neruda, Jan : O Šimonu Lomnickém. n=317
            '0692_0002-0001-0000-0003-0003' : '0742_0-0000-0000-0016-0000',    # (P7) Neruda, Jan : O ŠIMONU LOMNICKÉM (3) n=28
            '0692_0002-0001-0000-0003-0004' : '0742_0-0000-0000-0016-0000',    # (P8) Neruda, Jan : O ŠIMONU LOMNICKÉM (4) n=70
            # Chain of reworking 
            # => Keep longest and oldest version (P1)
            '0746_0-0002-0000-0082-0000'    : False,                           # (P1) Sládek, Josef Václav : Na hrobech Indianských. n=122 
            '0881_0001-0000-0000-0010-0000' : '0746_0-0002-0000-0082-0000',    # (P2) Sládek, Josef Václav : NA HROBECH INDIANSKÝCH. n=87
            '0889_0001-0000-0000-0011-0000' : '0746_0-0002-0000-0082-0000',    # (P3) Sládek, Josef Václav : NA HROBECH INDIANSKÝCH. n=87
            # Poem is published twice as a whole (P1, P2) and then once splitted into parts.
            # => Keep the oldest version (P1)            
            '0175_0001-0000-0000-0008-0000' : False,                           # (P1) Havlíček Borovský, Karel : Jus regale. n=7
            '0176_0001-0002-0000-0010-0000' : '0175_0001-0000-0000-0008-0000', # (P2) Havlíček Borovský, Karel : Jus Regale. n=7
            '0174_0001-0002-0002-0010-0001' : '0175_0001-0000-0000-0008-0000', # (P3) Havlíček Borovský, Karel : IUS REGALE (Professor iuris examinans dicit:) n=3
            '0174_0001-0002-0002-0010-0002' : '0175_0001-0000-0000-0008-0000', # (P4) Havlíček Borovský, Karel : IUS REGALE (Studiosus respondens dicit:) n=2
            # Poem is published twice: once as a whole (P3) and then splitted into two poems, yet whole
            # is published in a longer lines, hence has the same length as P1
            # => Keep whole text
            '0363_0001-0003-0000-0001-0001' : '0364_0001-0002-0000-0026-0000', # (P1) Karásek ze Lvovic, Jiří : VYHNANCŮM LÁSKY (1.) n=9
            '0363_0001-0003-0000-0001-0002' : '0364_0001-0002-0000-0026-0000', # (P2) Karásek ze Lvovic, Jiří : VYHNANCŮM LÁSKY (2.) n=7
            '0364_0001-0002-0000-0026-0000' : False,                           # (P3) Karásek ze Lvovic, Jiří : VYHNANCŮM LÁSKY n=9
            # Chain of reworking 
            # => Keep the oldest version (P1)
            '1105_0001-0004-0000-0007-0000' : False,                           # (P1) z Wojkowicz, Jan : Undina. n=29
            '1106_0001-0000-0000-0068-0000' : '1106_0001-0000-0000-0068-0000', # (P2) z Wojkowicz, Jan : UNDINA. n=29
            '1102_0001-0003-0001-0006-0000' : '1106_0001-0000-0000-0068-0000', # (P3) z Wojkowicz, Jan : UNDINA. n=31
            # Three times published as whole, three times splitted into three parts
            # => Keep the oldest and longest version (P1)   
            '1458_0001-0006-0000-0001-0000' : False,                           # (P1)  Bezruč, Petr : Já. 1903 n=136
            '1485_0001-0000-0000-0022-0000' : '1458_0001-0006-0000-0001-0000', # (P2)  Bezruč, Petr : JÁ 1967 n=133
            '1655_0001-0000-0000-0043-0003' : '1458_0001-0006-0000-0001-0000', # (P3)  Bezruč, Petr : JÁ (III) 1909 n=32
            '1656_0001-0000-0000-0052-0003' : '1458_0001-0006-0000-0001-0000', # (P4)  Bezruč, Petr : JÁ (III) 1957 n=31
            '1486_0001-0000-0000-0052-0002' : '1458_0001-0006-0000-0001-0000', # (P5)  Bezruč, Petr : JÁ (II) 1967 n=73
            '1460_0001-0000-0000-0051-0000' : '1458_0001-0006-0000-0001-0000', # (P6)  Bezruč, Petr : JÁ. 1911 n=134
            '1486_0001-0000-0000-0052-0003' : '1458_0001-0006-0000-0001-0000', # (P7)  Bezruč, Petr : JÁ (III) 1967 n=32
            '1655_0001-0000-0000-0043-0002' : '1458_0001-0006-0000-0001-0000', # (P8)  Bezruč, Petr : JÁ (II) 1909 n=72
            '1656_0001-0000-0000-0052-0002' : '1458_0001-0006-0000-0001-0000', # (P9)  Bezruč, Petr : JÁ (II) 1957 n=72
            '1486_0001-0000-0000-0052-0001' : '1458_0001-0006-0000-0001-0000', # (P10) Bezruč, Petr : JÁ (I) 1967 n=29
            '1655_0001-0000-0000-0043-0001' : '1458_0001-0006-0000-0001-0000', # (P11) Bezruč, Petr : JÁ (I) 1909 n=31
            '1656_0001-0000-0000-0052-0001' : '1458_0001-0006-0000-0001-0000', # (P12) Bezruč, Petr : JÁ (I) 1957 n=30
        }

    # ------------ DE ---------------------------------------------------------
    
    elif lang == 'de':
        
        return {
            # Basically just a single poem with some reworkings but dominantly concern omitting passages from middle
            # => Keep the longest P1
            '00-1734-0000-0002-405B-E#0' : False,                              # (P1) Brentano: [O Mutter halte dein Kindlein warm]
            '00-1734-0000-0002-41DA-8#0' : '00-1734-0000-0002-405B-E#0',       # (P2) Brentano: Meine Liebe an Sophien...
            '00-1734-0000-0002-40C3-F#0' : '00-1734-0000-0002-405B-E#0',       # (P3) Brentano: Gesang der Liebe...
            # These are all versions of the same poem just reworked 
            # => Keep the the longest P1
            '00-1734-0000-0003-7CB0-D#0' : False,                              # (P1) Hölderlin: Der Einzige
            '00-1734-0000-0003-7B04-A#0' : '00-1734-0000-0003-7CB0-D#0',       # (P2) Hölderlin: Der Einzige
            '00-1734-0000-0003-7A73-9#0' : '00-1734-0000-0003-7CB0-D#0',       # (P3) Hölderlin: Der Einzige
            # Chain of versions, P1 & P2 are of the same length, P3 is shorter
            # => keep the middle one (P2)
            '00-1734-0000-0003-7BCF-6#0' : '00-1734-0000-0003-7A0C-2#0',       # (P1) Hölderlin: An Eduard
            '00-1734-0000-0003-7A0C-2#0' : False,                              # (P2) Hölderlin: An Eduard
            '00-1734-0000-0003-7A32-A#0' : '00-1734-0000-0003-7A0C-2#0',       # (P3) Hölderlin: Die Dioskuren
            'dta.poem.4004'              : '00-1734-0000-0003-7A0C-2#0',       # (P3) Hölderlin: An Eduard
            # Angelus Silesius (all connected to metricalizer version)
            'dta.poem.23296'             : '00-1734-0000-0001-E9E7-E#0',      # (P1) Daß Ander. An die Jungfrau Maria die geheime Lilie    
            '00-1734-0000-0001-E9E7-E#0' : False,                             # (P2) An die Jungfrau Maria, die geheime Lilie      
            'dta.poem.17754'             : '00-1734-0000-0001-E9E7-E#0',      # (P3) 2. An die Jungfrau Maria die geheime Lilie.       
            'dta.poem.17755'             : '00-1734-0000-0001-E9E7-E#0',      # (P4) Sechstes Buch. Geistreicher Sinn- unnd Schluß reim
            # Clemens Brentano (similarity between P1 and P2 slightly below threshold but seems like a reworking)
            'dta.poem.3488'  : False,            # (P1) Einsiedler   
            'dta.poem.3588'  : 'dta.poem.3488',  # (P2) Der Knabe     
            'dta.poem.12457' : 'dta.poem.3488',  # (P3) Von Volksliedern  
            # Angelus Silesius (pick metricalizer version)
            'dta.poem.16645'             : '00-1734-0000-0001-F098-9#0',      # (P1) 4. Das Ewge Ja und Nein.     
            '00-1734-0000-0001-F098-9#0' : False,                             # (P2) 4. Das ewige Ja und Nein      
            'dta.poem.22203'             : '00-1734-0000-0001-F098-9#0',      # (P3) 4. Daß Ewge Ja und Nein.
            # Angelus Silesius (pick metricalizer version)
            'dta.poem.17761'             : '00-1734-0000-0001-E814-0#0',      # (P1) Sechstes Buch. Geistreicher Sinn- unnd Schluß reim    
            '00-1734-0000-0001-E814-0#0' : False,                             # (P2) 6. Überschrift der Verdammnis      
            'dta.poem.17760'             : '00-1734-0000-0001-E814-0#0',      # (P3) 6. Vberschrifft der Verdamnüß              
            'dta.poem.23300'             : '00-1734-0000-0001-E814-0#0',      # (P4) Daß Sechste Uberschrifft der Verdamnüß.
            # Hebel, Johann Peter
            "00-1734-0000-0003-42CA-6#0"   : False,                          # (P1) Der Karfunkel
            "dta.poem.20577"               : "00-1734-0000-0003-42CA-6#0",   # (P2) Der Carfunkel
            "dta.poem.20576"               : "00-1734-0000-0003-42CA-6#0",   # (P3) Der Carfunkel
            # Angelus Silesius
            "dta.poem.17884"               : "00-1734-0000-0001-E76C-3#0",   #(P1) 127. Der Liebe Todt und Pein.
            "dta.poem.22440"               : "00-1734-0000-0001-E76C-3#0",   #(P2) 244. Verachtet seyn bringt Wonne.
            "00-1734-0000-0001-E76C-3#0"   : False,                          #(P3) 280. Der wahre Weisen-Stein
            "dta.poem.16619"               : "00-1734-0000-0001-E76C-3#0",   #(P4) 280. Der wahre weisen Stein.
            "00-1734-0000-0001-F91A-A#0"   : "00-1734-0000-0001-E76C-3#0",   #(P5) 244. Verachtet sein bringt Wonne
            "dta.poem.16885"               : "00-1734-0000-0001-E76C-3#0",   #(P6) 244. Verrachtet seyn bringt Wonne.
            "dta.poem.22177"               : "00-1734-0000-0001-E76C-3#0",   #(P7) 280. Der wahre weisen Stein.
            "00-1734-0000-0001-F29F-9#0"   : "00-1734-0000-0001-E76C-3#0",   #(P8) 127. Der Liebe Tod und Pein
            # Angelus Silesius
            "00-1734-0000-0001-E5A4-4#0"   : False,                          #(P1) 4. Der gerechtfertigte Sünder
            "dta.poem.17757"               : "00-1734-0000-0001-E5A4-4#0",   #(P2) 4. Der Gerechtfertigte Sünder.
            "dta.poem.17758"               : "00-1734-0000-0001-E5A4-4#0",   #(P3) Sechstes Buch. Geistreicher Sinn- unnd Schluß reim
            "dta.poem.23298"               : "00-1734-0000-0001-E5A4-4#0",   #(P4) Daß Vierdte. Der Gerechtfertigte Sünder.
            # Herwegh, Georg
            "00-1734-0000-0003-5FFC-D#0"   : False,                          #(P1) 7.Frage
            "dta.poem.12496"               : "00-1734-0000-0003-5FFC-D#0",   #(P2) ViI. Frage .
            "dta.poem.12497"               : "00-1734-0000-0003-5FFC-D#0",   #(P3) ViI. Frage .
            # Gryphius, Andreas
            "00-1734-0000-0003-1AF9-6#0"   : False,                          #(P1) 27.Threnen des Vatterlandes/ Anno 1636
            "00-1734-0000-0003-1B16-B#0"   : "00-1734-0000-0003-1AF9-6#0",   #(P2) Trawrklage des verwüsteten Deutschlandes
            "dta.poem.741"                 : "00-1734-0000-0003-1AF9-6#0",   #(P3) XxVII. Thränen deß Vatterlandes Anno 1636.
            # Klopstock, Friedrich Gottlieb
            "dta.poem.8110"                : "00-1734-0000-0003-B4E6-6#0",   #(P1) 3.
            "dta.poem.8131"                : "00-1734-0000-0003-B4E6-6#0",   #(P2) 8.
            "dta.poem.8132"                : "00-1734-0000-0003-B4E6-6#0",   #(P3) 9.
            "dta.poem.8138"                : "00-1734-0000-0003-B4E6-6#0",   #(P4) 15.
            "dta.poem.8144"                : "00-1734-0000-0003-B4E6-6#0",   #(P5) Der Messias. Zwanzigster Gesang .
            "00-1734-0000-0003-B4E6-6#0"   : "00-1734-0000-0003-B4E6-6#0",   #(P6) Zwanzigster Gesang
            "dta.poem.8124"                : "00-1734-0000-0003-B4E6-6#0",   #(P7) 1.
            # Angelus Silesius
            "00-1734-0000-0001-EFF3-4#0"   : False,                          #(P1) 28. Der allerseligste Tod
            "dta.poem.16367"               : "00-1734-0000-0001-EFF3-4#0",   #(P2) 28. Der allerseeligste Tod.
            "dta.poem.21927"               : "00-1734-0000-0001-EFF3-4#0",   #(P3) 28. Der allerseeligste Todt.
            # Hölderlin, Friedrich
            "dta.poem.4062"                : "00-1734-0000-0003-7A25-8#0",   #(P1) 8.
            "00-1734-0000-0003-7A25-8#0"   : False,                          #(P2) Menons Klagen um Diotima
            "dta.poem.4063"                : "00-1734-0000-0003-7A25-8#0",   #(P3) 9.
            "00-1734-0000-0003-7BB2-4#0"   : "00-1734-0000-0003-7A25-8#0",   #(P4) Elegie
            "dta.poem.4055"                : "00-1734-0000-0003-7A25-8#0",   #(P5) 1.
            "dta.poem.4061"                : "00-1734-0000-0003-7A25-8#0",   #(P6) 7.
            "dta.poem.4060"                : "00-1734-0000-0003-7A25-8#0",   #(P7) 6.
            "dta.poem.4056"                : "00-1734-0000-0003-7A25-8#0",   #(P8) 2.
            "dta.poem.4059"                : "00-1734-0000-0003-7A25-8#0",   #(P9) 6.
            "dta.poem.4058"                : "00-1734-0000-0003-7A25-8#0",   #(P10) 4.
            "dta.poem.4057"                : "00-1734-0000-0003-7A25-8#0",   #(P11) 3.
            # Gryphius, Andreas
            "00-1734-0000-0003-17B6-1#0"   : "00-1734-0000-0003-1EB4-4#0",   #(P1) In Reverendi Clariss. Doctissimiq; Domini M. Pauli
            "00-1734-0000-0003-1EB4-4#0"   : False,                          #(P2) 15.In admodum Reverend. Nobiliss. Excellentiss. Do
            "dta.poem.729"                 : "00-1734-0000-0003-1EB4-4#0",   #(P3) Xv. In admodum Reverend. Nobiliß. Excellentiß. Dom
            # Brockes, Barthold Heinrich
            "dta.poem.4415"                : "00-1734-0000-0002-449E-3#0",   #(P1) Gottes Grösse in den Wassern.
            "dta.poem.11061"               : "00-1734-0000-0002-449E-3#0",   #(P2) Aus dem 18. Psalm, vom 8. bis 16. Vers.
            "dta.poem.4322"                : "00-1734-0000-0002-449E-3#0",   #(P3) Die schreckliche Gewalt des Wassers.
            "00-1734-0000-0002-449E-3#0"   : False,                          #(P4) Gottes Grösse in den Wassern
            # Gryphius, Andreas
            "dta.poem.740"                 : False,                          #(P1) XxVI. An Lucinden.
            "00-1734-0000-0003-1B40-9#0"   : "00-1734-0000-0003-1B40-9#0",   #(P2) 26.An Lucinden
            "00-1734-0000-0003-1AFE-B#0"   : "00-1734-0000-0003-1B40-9#0",   #(P3) An eine Jungfraw
            # Fontane, Theodor
            "dta.poem.20119"               : "00-1734-0000-0002-AEAE-6#0",   #(P1) Die Bienenschlacht.
            "dta.poem.20120"               : "00-1734-0000-0002-AEAE-6#0",   #(P2) Die Bienenschlacht.
            "00-1734-0000-0002-AEAE-6#0"   : False,                          #(P3) Bienen-Winkelried
            # Gryphius, Andreas
            "00-1734-0000-0003-1942-8#0"   : "00-1734-0000-0003-19D4-D#0",   #(P1) An Gott den Heiligen Geist
            "dta.poem.715"                 : "00-1734-0000-0003-19D4-D#0",   #(P2) I. An GOTT den Heiligen Geist.
            "00-1734-0000-0003-19D4-D#0"   : False,                          #(P3) 1.An Gott den Heiligen Geist
            # Zinzendorf, Nikolaus Ludwig von
            "dta.poem.19119"               : "00-1734-0000-0005-B5CD-3#0",   #(P1) Judith Kunertin. Eine Jungfrau von 50. Jahren, wel
            "dta.poem.19118"               : "00-1734-0000-0005-B5CD-3#0",   #(P2) C. Auf vier theure Mitglieder unsrer Ge- meine, so
            "dta.poem.19121"               : "00-1734-0000-0005-B5CD-3#0",   #(P3) Paul Schindler. Ein 67. jähriger Mann, der seinen.
            "dta.poem.19122"               : "00-1734-0000-0005-B5CD-3#0",   #(P4) Rosina Pischin. Eine Fran von 24. Jahren, die eine
            "dta.poem.19120"               : "00-1734-0000-0005-B5CD-3#0",   #(P5) Georg Seyfert. Ein Mann von etliche und 80. Jahren
            "00-1734-0000-0005-B885-B#0"   : "00-1734-0000-0005-B5CD-3#0",   #(P6) 68. Als es gleich jährig war, daß sein Herr Schwag
            "00-1734-0000-0005-B5CD-3#0"   : False,                          #(P7) 102. Auf vier theure Mitglieder unsrer Gemeine, so
            # Brockes, Barthold Heinrich
            "dta.poem.5435"                : "00-1734-0000-0002-4531-D#0",   #(P1) J rdisches V ergnügen in GOTT . F ünfter T heil.
            "00-1734-0000-0002-4531-D#0"   : False,                          #(P2) Alart
            "dta.poem.5434"                : "00-1734-0000-0002-4531-D#0",   #(P3) Alart.
            # Hölderlin, Friedrich
            "dta.poem.4008"                : "00-1734-0000-0003-7BB6-B#0",  #(P1) Stimme des Volks .
            "00-1734-0000-0003-7BB6-B#0"   : False,                         #(P2) Stimme des Volks
            "00-1734-0000-0003-7C11-4#0"   : "00-1734-0000-0003-7BB6-B#0",  #(P3) Stimme des Volks
            # Angelus Silesius
            "00-1734-0000-0001-F98F-4#0"   : False,                          #(P1) 146. Gott liebt nichts außer Christo
            "dta.poem.22045"               : "00-1734-0000-0001-F98F-4#0",   #(P2) 146. Gott liebt nichts ausser Christo.
            "dta.poem.16485"               : "00-1734-0000-0001-F98F-4#0",   #(P3) 146. GOtt liebt nichts ausser Christo.
            # Gryphius, Andreas
            "dta.poem.721"                 : "00-1734-0000-0003-1F86-4#0",   #(P1) ViI. Gedenckt an Loths Weib. Luc. 17. v. 32. Bauhu
            "00-1734-0000-0003-1961-2#0"   : "00-1734-0000-0003-1F86-4#0",   #(P2) Gedencket an des Loths Weib
            "00-1734-0000-0003-1F86-4#0"   : False,                          #(P3) 7.Gedencket an Loths Weib
            # Gryphius, Andreas
            "00-1734-0000-0003-1EC6-B#0"   : False,                         #(P1) 23.Auff Herrn Joachimi Spechts Hochzeitt
            "dta.poem.737"                 : "00-1734-0000-0003-1EC6-B#0",  #(P2) XxIII. Auff Herrn Joachimi Spechts Hochzeit.
            "00-1734-0000-0003-1F2D-C#0"   : "00-1734-0000-0003-1EC6-B#0",  #(P3) Auff Herrn Joachim Spechts vornehmen Medici vnd Ph
            # Gryphius, Andreas
            "00-1734-0000-0003-1A13-A#0"   : "00-1734-0000-0003-1F59-A#0",  #(P1) An den am Creutz auffgehenckten Heyland
            "00-1734-0000-0003-1F59-A#0"   : False,                         #(P2) 6.An den gecreutzigten Jesum
            "dta.poem.720"                 : "00-1734-0000-0003-1F59-A#0",  #(P3) Vi. An den geereutzigten Jesum. Sarbievij: Hincut 
            # Gryphius, Andreas
            "00-1734-0000-0003-1B21-2#0"   : False,                         #(P1) 31.An Furium
            "00-1734-0000-0003-1DBE-7#0"   : "00-1734-0000-0003-1B21-2#0",  #(P2) An einen falschen Zwey-züngeler
            "dta.poem.745"                 : "00-1734-0000-0003-1B21-2#0",  #(P3) XxXI. An Furium.
            # Gryphius, Andreas
            "dta.poem.731"                 : "00-1734-0000-0003-1A59-C#0",  #(P1) XvII. Vber seines Herrn Brudern Pauli Gryphij Geis
            "00-1734-0000-0003-1F94-4#0"   : "00-1734-0000-0003-1A59-C#0",  #(P2) Vber eben dessen Geistliches Schuld-Buch
            "00-1734-0000-0003-1A59-C#0"   : False,                          #(P3) 17.Vber seines Herrn Brudern Pauli Gryphii Geistli
        }
    
    # ------------ EN ---------------------------------------------------------
    
    elif lang == 'en':
        
        return {
            # P1 and P3 share some lines (mostly contained in P2) but they both add a lot
            # of different text. 
            'wordsworth-works3---31'         : False,                          # (P1) Wordsworth: BOOK FIFTH
            'wordsworth-works2---1'          : 'wordsworth-works3---31',       # (P2) Wordsworth: There was a boy
            'wordsworth-lyricalBallads2---2' : False,                          # (P3) Wordsworth: PART SECOND
            # P2 & P4 are two parts of P1 (connected to it), P3 is just like P1 but lot of parts omitted
            # in the middle (hence not connected)
            # => P2, P3, P4 all duplicates of P1    
            'riley-complete1---23' : False,                                    # (P1) Riley: An Old Sweetheart of Mine
            'riley-loveLyrics---1' : 'riley-complete1---23',                   # (P2) Riley: An Old Sweetheart of Mine
            'riley-pipes---25'     : 'riley-complete1---23',                   # (P3) Riley: An Old Sweetheart of Mine
            'riley-loveLyrics---2' : 'riley-complete1---23',                   # (P4) Riley: An Old Sweetheart of Mine
            # These are all parts of one poem - similar structure and vocabulary yet not duplicates
            # => Keep them all
            'oxenham-beesInAmber---78' : False,                                # (P1) Dunkerley: PROCESSIONALS
            'oxenham-beesInAmber---79' : False,                                # (P2) Dunkerley: East
            'oxenham-beesInAmber---80' : False,                                # (P3) Dunkerley: West
            'oxenham-beesInAmber---81' : False,                                # (P4) Dunkerley: South            
            # These are all parts of a single poem (refrains etc.)
            # => Keep them all, just adding remove here to not display them in the graph
            'noyes-collectedPoems1---48' : False,                              # (P1) Noyes: THE PROGRESS OF LOVE 
            'noyes-collectedPoems1---55' : False,                              # (P2) Noyes: VIII 
            'noyes-collectedPoems1---62' : False,                              # (P3) Noyes: XV 
            'noyes-collectedPoems1---63' : False,                              # (P4) Noyes: XVI        
        }
    
    # ------------ ES ---------------------------------------------------------
    
    elif lang == 'es':
    
        return {}
    
    # ------------ FR ---------------------------------------------------------
 
    elif lang == 'fr':
     
        return {}

    # ------------ HU ---------------------------------------------------------   
    
    elif lang == 'hu':
        
        return {

            # P3 is the longest one (8k lines), P1 (1.5k) are pieces of P3 with skips, 
            # P2 is just a small piece from both
            # => Keep only P3          
            'AranyJ_00597_1133' : 'AranyJ_00597_1306',     # (P1) Arany: Daliás idők [2]
            'AranyJ_00597_0194' : 'AranyJ_00597_1306',     # (P2) Arany: ZÁCH KLÁRA
            'AranyJ_00597_1306' : False,                   # (P3) Arany: Toldi szerelme
            # This seems like a chain of reworking, P1 is shortest, P2 and P3 are of the same length
            # => keep P2         
            'Csokonai_00636_0187' : 'Csokonai_00636_0137', # (P1) Csokonai: [Falataimat elegyes borhajtással...]
            'Csokonai_00636_0137' : False,                 # (P2) Csokonai: Az Ekhóhoz [1]
            'Csokonai_00636_0227' : 'Csokonai_00636_0137', # (P3) Csokonai: Az Ekhóhoz [2]            
        }
    
    # ------------ IT ---------------------------------------------------------
    
    if lang == 'it':
        
        return {
    
            # = Torquato Tasso
            'bibit000099-108' : False,              # all same length - random
            'bibit001390-31'  : 'bibit000099-108',
            'bibit000256-31'  : 'bibit000099-108',
            'bibit000682-72'  : 'bibit000099-108',
            'bibit001217-108' : 'bibit000099-108',
           
            'bibit000260-10'  : False,              # longest
            'bibit000540-3'   : 'bibit000260-10', 
            'bibit001501-9'   : 'bibit000260-10',         
 
            'bibit001217-19'  : False,              # all same length - random
            'bibit001315-2'   : 'bibit001217-19', 
            'bibit000682-8'   : 'bibit001217-19',
            'bibit000099-19'  : 'bibit001217-19',

            'bibit000260-15'  : False,              # longest
            'bibit000540-4'   : 'bibit000260-15', 
            'bibit001501-12'  : 'bibit000260-15',

            # = Francesco Petrarca            
            'bibit000509-6'   : False,              # one of the longest two
            'bibit000509-17'  : 'bibit000509-6', 
            'bibit000756-12'  : 'bibit000509-6', 
            'bibit001257-71'  : 'bibit000509-6',

            'bibit000756-11'  : False,              # all same length - random
            'bibit001257-67'  : 'bibit000756-11', 
            'bibit000509-9'   : 'bibit000756-11', 
            'bibit001257-68'  : 'bibit000756-11',

            # = Ugo Foscolo
            'bibit000187-21'  : False,              # longest
            'bibit000187-8'   : 'bibit000187-21', 
            'bibit000187-34'  : 'bibit000187-21',     
            
            'bibit000412-72'  : False,              # longest
            'bibit000412-74'  : 'bibit000412-72', 
            'bibit000412-68'  : 'bibit000412-72', 
            
            # = Vincenzo Monti            
            'bibit000696-112' : False,              # longest
            'bibit000696-111' : 'bibit000696-112', 
            'bibit000430-16'  : 'bibit000696-112',
            
            # = Luigi Tansillo
            'bibit001584-1'   : False,              # longest
            'bibit001629-147' : 'bibit001584-1', 
            'bibit001631-203' : 'bibit001584-1',  
         }          
 
    # ------------ PT ---------------------------------------------------------
    
    elif lang == 'pt':
    
        return {}
    
    # ------------ RU ---------------------------------------------------------
    
    elif lang == 'ru':
        
        return {
            
            # Even though not a complete component, these are all versions of the Imperial
            # Russia anthem
            # => keep the longest one (P3)            
            'pu-coll-03' : 'zhuk-333',   # (P1) Pushkin + Zhukovskij: «Боже! царя храни!..»
            'zhuk-177'   : 'zhuk-333',   # (P2) Zhukovskij: Молитва русского народа | «Боже, Царя храни!...»
            'zhuk-333'   : False,        # (P3) Zhukovskij: Молитва русского народа | «Боже, Царя храни!...»
            'zhuk-491'   : 'zhuk-333',   # (P4) Zhukovskij: «Боже, Царя храни...»
            'zhuk-494'   : 'zhuk-333',   # (P5) Zhukovskij: Песня русских солдат | «Боже! Царя храни!...»
            
        }

    
    # ------------ SL ---------------------------------------------------------
    
    elif lang == 'sl':
    
        return {}