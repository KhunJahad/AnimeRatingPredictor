import re


text = """
NAME                                    READY   STATUS    RESTARTS   AGE
svclb-postgres-mq-load-balancer-f6hck   1/1     Running   0          73m
rasa-db-migration-service-0             1/1     Running   1          56m
svclb-postgres-mq-load-balancer-tbpgh   1/1     Running   1          73m
rasa-redis-master-0                     1/1     Running   1          56m
rasa-postgresql-0                       1/1     Running   1          56m
rasa-event-service-6764f865f6-jlb7v     1/1     Running   0          31m
rasa-nginx-7446b76598-bmm8m             1/1     Running   0          31m
rasa-app-6f9789bbd6-f86ks               1/1     Running   0          31m
rasa-rasa-worker-c77b7f469-xhpbv        1/1     Running   0          30m
rasa-rasa-x-6ff85965b-222wh             1/1     Running   0          30m
rasa-rasa-production-68f987fdcd-56dbv   1/1     Running   1          30m
rasa-rabbit-0                           1/1     Running   0          30m
CompletedProcess(args=['kubectl', 'get', 'pods', '-n', 'rasa'], returncode=0)
"""

names=re.findall("rasa-[^\s]+",text)
print(names)