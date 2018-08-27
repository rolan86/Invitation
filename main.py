from invitation.compute import new_compute as nc


if __name__ == '__main__':
    obj = nc.Invite()
    data = obj.get_data('data/data.json')
    fdata = obj.format_data(data)
    for uid, name, distance in obj.get_invitees(fdata):
        print "{}. {} is {} away from your location" .format(
            uid, name, distance
        )
