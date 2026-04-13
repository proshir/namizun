from namizun_core.paths import log_path
from namizun_core.time import get_now_date, get_now_time
from namizun_core.network import get_size


def _append_log_line(line):
    with open(log_path(), 'a', encoding='UTF-8') as log_file:
        log_file.write(line)


def store_restart_namizun_uploader_log():
    _append_log_line(
        f"date: {get_now_date()} - "
        f"time: {get_now_time()} - "
        f"namizun.service restarted\n"
    )


def store_new_upload_loop_log(total_uploader_count, total_upload_size):
    _append_log_line(
        f"date: {get_now_date()} - "
        f"time: {get_now_time()} - "
        f"new upload loop started - "
        f"[total uploader count: {total_uploader_count} - "
        f"total upload size: {get_size(total_upload_size)}]\n"
    )


def store_new_upload_agent_log(uploader_count, upload_size_for_each_ip):
    _append_log_line(
        f"date: {get_now_date()} - "
        f"time: {get_now_time()} - "
        f"new upload agent started - "
        f"[uploader count: {uploader_count} - "
        f"upload size for each ip: {get_size(upload_size_for_each_ip)}]\n"
    )


def store_new_udp_uploader_log(started_at, target_ip, target_port, upload_size, ended_at):
    _append_log_line(
        f"date: {get_now_date()} - "
        f"udp uploader - "
        f"[start: {started_at} - "
        f"ip: {target_ip} - "
        f"port: {target_port} - "
        f"size: {get_size(upload_size)} - "
        f"finish: {ended_at}]\n"
    )
