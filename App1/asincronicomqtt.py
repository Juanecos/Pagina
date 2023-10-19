import asyncio
import aiomqtt
import ssl
import sys
import os

if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

async def main():
    clientenuevo=aiomqtt.Client(
        hostname="6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud",  # El parámetro no opcional
        port=8883,
        username='juan-camilo',
        password='iNM123456789',
        logger=None,
        client_id=None,
        # tls_context= ssl.SSLContext,
        tls_context=None,
        tls_params = aiomqtt.TLSParameters(
            ca_certs=None,
            certfile=None,
            keyfile=None,
            cert_reqs=ssl.CERT_REQUIRED,
            tls_version=ssl.PROTOCOL_TLS,
            ciphers=None,
        ),
        # tls_params=None,
        tls_insecure=False,
        proxy=None,
        protocol=None,
        will=None,
        clean_session=True,
        transport="tcp",
        keepalive=60,
        bind_address="",
        bind_port=0,
        clean_start=3,
        properties=None,
        message_retry_set=20,
        socket_options=None,
        max_concurrent_outgoing_calls=None,
        websocket_path=None,
        websocket_headers=None,
        max_inflight_messages=None,
        max_queued_messages=None
    )
    async with clientenuevo as client:
        # await client.publish("temperature/outside", payload=28.4)
        async with client.messages() as messages:
            await client.subscribe("temperatura1")
            async for message in messages:
                print(message.payload)
asyncio.run(main())
# if __name__ == '__main__':


# Change to the "Selector" event loop if platform is Windows
# Run your async application as usual



# asyncio.run(main())