
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy import create_engine



db = SQLAlchemy(app)



from app.dbmodel import isimModule

from app.dbmodel import k8sconfig



exists = k8sconfig.query.filter_by(name='bitbucketusername').first()
if not exists:
	conf = k8sconfig()
	conf.name='bitbucketusername'
	conf.config=''
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='bitbucketpassword').first()
if not exists:
	conf = k8sconfig()
	conf.name='bitbucketpassword'
	conf.config=''
	db.session.add(conf)
	db.session.commit()	


exists = k8sconfig.query.filter_by(name='nvr1').first()
if not exists:
	conf = k8sconfig()
	conf.name='nvr1'
	conf.config='172.16.166.148'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='nvr2').first()
if not exists:
	conf = k8sconfig()
	conf.name='nvr2'
	conf.config='172.16.166.149'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='nvr3').first()
if not exists:
	conf = k8sconfig()
	conf.name='nvr3'
	conf.config='172.16.166.150'
	db.session.add(conf)
	db.session.commit()



exists = k8sconfig.query.filter_by(name='gateway').first()
if not exists:
	conf = k8sconfig()
	conf.name='gateway'
	conf.config='172.16.166.1'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='netmask').first()
if not exists:
	conf = k8sconfig()
	conf.name='netmask'
	conf.config='255.255.255.0'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='ipblockstart').first()
if not exists:
	conf = k8sconfig()
	conf.name='ipblockstart'
	conf.config='172.16.166.100'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='ipblockend').first()
if not exists:
	conf = k8sconfig()
	conf.name='ipblockend'
	conf.config = '172.16.166.150'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='installtype').first()
if not exists:
	conf = k8sconfig()
	conf.name='installtype'
	conf.config = 'offline'
	db.session.add(conf)
	db.session.commit()

exists = k8sconfig.query.filter_by(name='repourl').first()
if not exists:
	conf = k8sconfig()
	conf.name='repourl'
	conf.config = 'bitbucket.org/isimplatform/fullisimstack-helm.git'
	db.session.add(conf)
	db.session.commit()	

exists = isimModule.query.filter_by(name='arangodb').first()
if not exists:
	conf = isimModule()
	conf.name='arangodb'
	conf.defaultval = 'true'
	conf.val='0,1.0.92'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='bluetooth-engine').first()
if not exists:
	conf = isimModule()
	conf.name='bluetooth-engine'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='bluetooth-integrator').first()
if not exists:
	conf = isimModule()
	conf.name='bluetooth-integrator'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='cabinet-engine').first()
if not exists:
	conf = isimModule()
	conf.name='cabinet-engine'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='cabinet-integration').first()
if not exists:
	conf = isimModule()
	conf.name='cabinet-integration'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='connectors').first()
if not exists:
	conf = isimModule()
	conf.name='connectors'
	conf.defaultval = 'true'
	conf.val='cabinet_datas, weathersensor_datas,bluetooth_travel_averages,maintenance_topic,bluetooth_devices,cabinet_alarms,bluetooth_travels'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='coturn').first()
if not exists:
	conf = isimModule()
	conf.name='coturn'
	conf.defaultval = 'true'
	conf.val='172.16.160.112,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='dmiintegstring').first()
if not exists:
	conf = isimModule()
	conf.name='dmiintegstring'
	conf.defaultval = 'true'
	conf.val='brand%Proline,model%default,url%http://dmsintegrator.default.svc.isim.internal:9002'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='dms-engine').first()
if not exists:
	conf = isimModule()
	conf.name='dms-engine'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='domainname').first()
if not exists:
	conf = isimModule()
	conf.name='domainname'
	conf.defaultval = 'true'
	conf.val='devk8s.isimplatform.io'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='elasticsearch').first()
if not exists:
	conf = isimModule()
	conf.name='elasticsearch'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='erebor').first()
if not exists:
	conf = isimModule()
	conf.name='erebor'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='geoserver').first()
if not exists:
	conf = isimModule()
	conf.name='geoserver'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='hayda-engine').first()
if not exists:
	conf = isimModule()
	conf.name='hayda-engine'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='hayda-integration').first()
if not exists:
	conf = isimModule()
	conf.name='hayda-integration'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='haydaintegstring').first()
if not exists:
	conf = isimModule()
	conf.name='haydaintegstring'
	conf.defaultval = 'true'
	conf.val='brand%Proline,model%default,url%http://hayda-integration.default.svc.isim.internal:4002@brand%ortana,model%default,url%http://172.16.160.109:9003'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='imanager').first()
if not exists:
	conf = isimModule()
	conf.name='imanager'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='isimbackups').first()
if not exists:
	conf = isimModule()
	conf.name='isimbackups'
	conf.defaultval = 'true'
	conf.val='yes'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='isimcdn').first()
if not exists:
	conf = isimModule()
	conf.name='isimcdn'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='isimclient').first()
if not exists:
	conf = isimModule()
	conf.name='isimclient'
	conf.defaultval = 'true'
	conf.val='172.16.135.240,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='isimcore').first()
if not exists:
	conf = isimModule()
	conf.name='isimcore'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='isimdbstr').first()
if not exists:
	conf = isimModule()
	conf.name='isimdbstr'
	conf.defaultval = 'true'
	conf.val='crx7SZJmsgG8AAbPsP1sTXoSLwMqDIiF6vOgBordHYYWCqODl/eqEaKxd642SYbL wxcJnlAZ85PdU5kKnOOqrCPMe3Ux/Oqw7k1/HJDMCefjD7ILmXS/OW38qmUknwHp NMzVP2uxcixbOYnwSwgcLr7t+7kkrrUkT4VWxW/7H6woc4xkkfcF+umuerLjQXHX A0sU6mK62ePRHsu5lcqNWaRH1/U6uB4CfuJSWP1BxwQ'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='isim-print-server').first()
if not exists:
	conf = isimModule()
	conf.name='isim-print-server'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='kafka-connect').first()
if not exists:
	conf = isimModule()
	conf.name='kafka-connect'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='kibana').first()
if not exists:
	conf = isimModule()
	conf.name='kibana'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='kurento').first()
if not exists:
	conf = isimModule()
	conf.name='kurento'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='kurento-room-server').first()
if not exists:
	conf = isimModule()
	conf.name='kurento-room-server'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='librenms').first()
if not exists:
	conf = isimModule()
	conf.name='librenms'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='loglevel').first()
if not exists:
	conf = isimModule()
	conf.name='loglevel'
	conf.defaultval = 'true'
	conf.val='3'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='logstash').first()
if not exists:
	conf = isimModule()
	conf.name='logstash'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='lomanager').first()
if not exists:
	conf = isimModule()
	conf.name='lomanager'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='mongo').first()
if not exists:
	conf = isimModule()
	conf.name='mongo'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='mosquitto').first()
if not exists:
	conf = isimModule()
	conf.name='mosquitto'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='multusnet').first()
if not exists:
	conf = isimModule()
	conf.name='multusnet'
	conf.defaultval = 'true'
	conf.val='172.16.160.141-172.16.160.142,172.16.160.0/22,172.16.160.1'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='nazgul').first()
if not exists:
	conf = isimModule()
	conf.name='nazgul'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='nominatim').first()
if not exists:
	conf = isimModule()
	conf.name='nominatim'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='nova').first()
if not exists:
	conf = isimModule()
	conf.name='nova'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='novapp').first()
if not exists:
	conf = isimModule()
	conf.name='novapp'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='ntpproxy').first()
if not exists:
	conf = isimModule()
	conf.name='ntpproxy'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='ntpserver').first()
if not exists:
	conf = isimModule()
	conf.name='ntpserver'
	conf.defaultval = 'true'
	conf.val='ntp.pool.org'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='optimusprime').first()
if not exists:
	conf = isimModule()
	conf.name='optimusprime'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='plato').first()
if not exists:
	conf = isimModule()
	conf.name='plato'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='postgis').first()
if not exists:
	conf = isimModule()
	conf.name='postgis'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='prometheus').first()
if not exists:
	conf = isimModule()
	conf.name='prometheus'
	conf.defaultval = 'true'
	conf.val='yes'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='redis').first()
if not exists:
	conf = isimModule()
	conf.name='redis'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='reimdall').first()
if not exists:
	conf = isimModule()
	conf.name='reimdall'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='rest-proxy').first()
if not exists:
	conf = isimModule()
	conf.name='rest-proxy'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='riemann').first()
if not exists:
	conf = isimModule()
	conf.name='riemann'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='riemanngo').first()
if not exists:
	conf = isimModule()
	conf.name='riemanngo'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='riemanngostorage').first()
if not exists:
	conf = isimModule()
	conf.name='riemanngostorage'
	conf.defaultval = 'true'
	conf.val='{"name": "container", "path": "flows"}'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='riemannnvr').first()
if not exists:
	conf = isimModule()
	conf.name='riemannnvr'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='riemannui').first()
if not exists:
	conf = isimModule()
	conf.name='riemannui'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='saruman').first()
if not exists:
	conf = isimModule()
	conf.name='saruman'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='sslenabled').first()
if not exists:
	conf = isimModule()
	conf.name='sslenabled'
	conf.defaultval = 'true'
	conf.val='no'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='videogw').first()
if not exists:
	conf = isimModule()
	conf.name='videogw'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='videogwdotnet').first()
if not exists:
	conf = isimModule()
	conf.name='videogwdotnet'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='videogwinteg').first()
if not exists:
	conf = isimModule()
	conf.name='videogwinteg'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='weyland').first()
if not exists:
	conf = isimModule()
	conf.name='weyland'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='zonemanager').first()
if not exists:
	conf = isimModule()
	conf.name='zonemanager'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()



exists = isimModule.query.filter_by(name='zookeeper').first()
if not exists:
	conf = isimModule()
	conf.name='zookeeper'
	conf.defaultval = 'true'
	conf.val='0,0'
	db.session.add(conf)
	db.session.commit()