# Attempt


# Message bus paths

Loadbalancing > LTM > {ADD,CHANGE,DELETE}
Loadbalancing > WIP > {ADD,CHANGE,DELETE} #Loadbalancing.WIP.ADD, Loadbalancing.WIP.DELETE, Loadbalancing.WIP.CHANGE

VirtualTopic.Loadbalancing.WIP.ADD
VirtualTopic.Loadbalancing.WIP.DELETE
VirtualTopic.Loadbalancing.WIP.CHANGE



View wip.json for message details



Subscribe to 
Loadbalancing.WIP.ADD

Subscribe to
Loadbalancing.WIP.*

Send 

New WIP to 
Loadbalancing.WIP.ADD
Modify WIP to
Loadbalancing.WIP.CHANGE
Delete WIP to
Loadbalancing.WIP.DELETE